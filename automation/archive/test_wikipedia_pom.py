from automation.pages.wikipedia_homepage import WikipediaHomePage

def test_content_present(driver):
    wiki_page = WikipediaHomePage(driver)
    wiki_page.load()
    wiki_page.search("Python")
    assert wiki_page.verify_content(), "El texto esperado no se encontró en la página"