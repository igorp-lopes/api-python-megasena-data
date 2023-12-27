from playwright.async_api import async_playwright

from src.app.core.config import MEGA_SENA_DATA_URL, MEGA_SENA_DATA_PATH
from src.app.services.mega_sena_data_service import MegaSenaDataService


class MegaSenaScrapperService:
    def __init__(self, mega_sena_data_service: MegaSenaDataService):
        self.mega_sena_data_service = mega_sena_data_service

    async def _download_mega_sena_data_file(self):
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
