import pandas as pd
from playwright.async_api import async_playwright

from src.app.core.config import MEGA_SENA_DATA_URL, MEGA_SENA_DATA_PATH
from src.app.entities.mega_sena_data_model import MegaSenaData
from src.app.services.mega_sena_data_service import MegaSenaDataService


class MegaSenaScrapperService:
    def __init__(self, mega_sena_data_service: MegaSenaDataService):
        self.mega_sena_data_service = mega_sena_data_service

    @staticmethod
    async def _download_mega_sena_data_file():
        async with async_playwright() as p:
            p.selectors.set_test_id_attribute("class")
            browser = await p.chromium.launch(headless=False)
            page = await browser.new_page()
            await page.goto(MEGA_SENA_DATA_URL)
            button = page.get_by_test_id("title zeta")

            async with page.expect_download() as download_info:
                await button.click()

            download = await download_info.value
            await download.save_as(MEGA_SENA_DATA_PATH)

    @staticmethod
    def _map_resource_to_mega_sena_records():
        df = pd.read_excel(MEGA_SENA_DATA_PATH)
        row = df.iloc[0]
        dicted = row.to_dict()
        dicted = {
            "concurso": 1,
            "data_do_sorteio": "1996-03-11",
            "bola1": 4,
            "bola2": 5,
            "bola3": 30,
            "bola4": 33,
            "bola5": 41,
            "bola6": 52,
            "ganhadores_6_acertos": 0,
            "rateio_6_acertos": "R$0,00",
            "ganhadores_5_acertos": 17,
            "rateio_5_acertos": "R$39.158,92",
            "ganhadores_4_acertos": 2016,
            "rateio_4_acertos": "R$330,21",
            "acumulado_6_acertos": "R$1.714.650,23",
            "arrecadacao_total": "R$0,00",
            "estimativa_premio": "R$0,00",
            "acumulado_sorteio_especial_mega_da_virada": "R$0,00",
        }
        return MegaSenaData.model_validate(dicted)

    async def test_save_mega_sena_record(self):
        # await self._download_mega_sena_data_file()
        data_to_save = self._map_resource_to_mega_sena_records()
        saved_data = await self.mega_sena_data_service._save_mega_sena_record(
            data_to_save
        )
        return saved_data
