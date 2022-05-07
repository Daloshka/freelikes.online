from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import sys
import vk_api

#################################Настройки###################################

LIKES_TIMES = 10				#Выполнений задания "Поставить лайк" подряд
VIEWS_TIMES = 10 				#Выполнений задания "Посмотреть видео" подряд
HEADLESS_MODE = True		    #Скрытый режим (True или False)
MUTE_AUDIO = True				#Отключить звук (True или False)
i = 0 
#############################################################################

if __name__ == "__main__":
	# if len (sys.argv) < 2:
	# 	print("Недостаточно параметров")
	# 	sys.exit()
    LOGIN = ""
    PASSWORD = ""
    VKURL = ""
    session = vk_api.VkApi(token= "")

def like():
    global i
    try:
        like_btn = driver.find_element_by_class_name("like_button_icon")[i]
        like_btn.click()
        sleep(2)
        driver.close()
        driver.switch_to.window(original_window)
        print(f"S {i}")
    except:
        i += 1
        print(f"Error {i}")

def login():
    print("\n Вход на сайт...")
    driver.get("http://freelikes.online/")
    original_window = driver.current_window_handle
    enter_field = driver.find_element_by_xpath("//*[@id='uLogin']/span[1]/i")
    enter_field.click()
    sleep(2)
    for handle in driver.window_handles:
        driver.switch_to.window(handle)

    login_field = driver.find_element_by_xpath("//*[@id='login_submit']/div/div/input[6]")
    login_field.click()
    login_field.send_keys(LOGIN)

    password_field = driver.find_element_by_xpath("//*[@id='login_submit']/div/div/input[7]")
    password_field.click()
    password_field.send_keys(PASSWORD)

    login_btn = driver.find_element_by_xpath('//*[@id="install_allow"]')
    login_btn.click()

    driver.switch_to.window(original_window) 
    driver.get("http://freelikes.online/earn/vkontakte/vklike")
    

    while True:
        link = driver.find_element_by_xpath('//*[@id="btnheight"]')
        link.click()
        window_vk = driver.window_handles[-1]
        driver.switch_to.window(window_vk)
        sleep(1)

        try:
            driver.find_element_by_css_selector('.like_button_icon').click()
            print("1")
            sleep(1)
        except:
            print(f"Error 1")
            try:
                driver.find_element_by_css_selector('.PostBottomAction__icon._like_button_icon').click()
                print("2")
                sleep(1)
            except:
                print(f"Error 2")
                try:
                    driver.find_element_by_css_selector('.PostBottomActionContainer.PostButtonReactionsContainer').click()
                    print("3")
                    sleep(1)
                except:
                    print(f"Error 3")
        
        
        sleep(2)
        print("here")
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        driver.get("http://google.com")
        driver.get("http://freelikes.online/earn/vkontakte/vklike")
        sleep(3)

    #     driver.switch_to.window(window_vk)
    #     print('he4')
    #     like()

    #like_button = get_element("yt-icon.style-scope.ytd-toggle-button-renderer")

    #session.method('wall.addLike', {'owner_id' :owner_id, 'post_id': post_id, 'random_id' : random.randint(1000, 99999)})
    #get_element("#identifierId")
    # get_element(".CwaK9").click()
    # get_element(".whsOnd.zHQkBf").send_keys(PASSWORD)
    # get_element(".CwaK9").click()
    sleep(1000)

def main():
    login()

options = webdriver.ChromeOptions()
# if HEADLESS_MODE: options.add_argument('--headless')
# if MUTE_AUDIO: options.add_argument("--mute-audio") 
# #options.add_argument("--disable-dev-shm-usage")
# options.add_argument("--log-level=3") 
driver = webdriver.Chrome("./chromedriver",chrome_options=options)
main()