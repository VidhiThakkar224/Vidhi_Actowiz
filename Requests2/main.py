from fetch import make_requests, save, run_threads
from parser import main_page_parse
from config import HOME_PAGE, PAGE_SAVE_DIR, THREADS


home_page_response = run_threads(thread_count=THREADS, args=('GET', HOME_PAGE))
if not home_page_response['error']:
    filepath = PAGE_SAVE_DIR + 'main.html'
    save(content=home_page_response['body'], path=filepath)
    main_page_parse(home_page_response['body'])
else:
    print(home_page_response['error'])