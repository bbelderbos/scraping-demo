from playwright.sync_api import sync_playwright

TRANSLATE_URL = (
    "https://salt.gva.es/auto/traductor-corrector/"
    "salt-traductor-va.html")


def translate_text(text, headless=True, slow_mo=1000):
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=headless, slow_mo=slow_mo)
        page = browser.new_page()
        page.goto(TRANSLATE_URL)
        page.locator('#traductor').fill(text.strip())
        page.locator('input[name="sentido"]').last.check()
        page.locator("#enviarText").click()
        translated_text = page.locator("#traductor_destino").input_value()
        return translated_text
