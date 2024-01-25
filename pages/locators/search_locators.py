from selenium.webdriver.common.by import By

search_results_grid = (By.XPATH, "//div[@data-zalon-partner-target='true']")
search_results_prices = (
    By.XPATH, "(//section[@class='_0xLoFW _78xIQ-']//p[1]//span[1])"
)
results_count = (
    By.XPATH, "(//span[@class='sDq_FX _2kjxJ6 FxZV-M Yb63TQ lystZ1 FxZV-M'])[1]")
search_title = (
    By.XPATH, "//span[@class='sDq_FX qQ75Zg FxZV-M HlZ_Tf CzGCn5']"
)
nothing_found = (
    By.XPATH, "//h1[@class='sDq_FX qQ75Zg FxZV-M HlZ_Tf']"
)
try_search_again = (
    By.XPATH, "//span[@class='FtrEr_ _4sa1cA dgII7d HlZ_Tf']"
)
sort = (
    By.XPATH,
    "//div[@class='Zhr-fS _9l1hln _65i7kZ']"
)
sort_by_price_low_to_high = (
    By.XPATH, "(//div[@class='_5Bccgc _0xLoFW JT3_zV FCIprz LyRfpJ'])[3]"
)
sort_by_price_high_to_low = (
    By.XPATH, "(//div[@class='_5Bccgc _0xLoFW JT3_zV FCIprz LyRfpJ'])[4]"
)
brand_filter = (
    By.XPATH, "//div[@class='Zhr-fS _65i7kZ _9l1hln JT3_zV TOJxrT catalog-filter'][2]"
)
brand_filter_search = (
    By.XPATH, "//div[@class='AcNrW- zXJU72 _0xLoFW _78xIQ-']"
)
brand_filter_search_input = (
    By.XPATH, "//input[@name='brand-filter-search']"
)
brand_filter_search_first_result = (
    By.XPATH, "(//div[@class='KnR7WS _0xLoFW JT3_zV FCIprz LyRfpJ'])[1]"
)
brand_filter_search_submit = (
    By.XPATH, "(//div[@class='_0xLoFW _4qpPat _9bx9k9']//button)[2]"
)