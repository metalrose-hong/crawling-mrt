from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import requests
import time
from furl import furl

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.binary_location = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
chrome_driver_path = ('/Users/XXXXXXXX/crawling-mrt/chromedriver')  # PATH 수정

if __name__ == '__main__':
    try:
        # 크롬을 헤드리스 모드로 실행
        driver = webdriver.Chrome(chrome_driver_path, chrome_options=chrome_options)

        # 스크레이핑 대상 URL 지정
        target_url = 'https://www.myrealtrip.com/offers/2654'
        # 헤드리스 모드 크롬으로 스크레이핑 대상 페이지 열기
        driver.get(target_url)

        # 내부적으로 Ajax를 사용해서 처리하는 경우
        # 화면을 모두 읽어 들일 때까지 어느 정도 대기해야 합니다.
        time.sleep(2)

        # 제목 요소를 CSS 선택자로 지정해서 추출합니다.
        title = driver.find_elements_by_css_selector('.offer-container__title')[0].text

        print(title)

    except Exception as e:
        # 예외가 발생했을 경우 스택 트레이스를 출력합니다.
        print(e)

    finally:
        # 예외가 발생해서 프로그램이 종료됐을 때
        # 크롬 프로세스가 남는 것을 피할 수 있게 finally 구문 내부에서 종료해줍니다.
        driver.close()
