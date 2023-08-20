# # # # # # # # # # # # # # # # # # # # # #
# This script searches all the admission  #
# numbers for which the TC data is yet to #
# be upload on the KVS website and stores #
# it in a file for further use.           #
# # # # # # # # # # # # # # # # # # # # # #

import argparse
import sys
from urllib.parse import urlparse

# command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('url', type=str, help='Kendriya vidyalaya url')
parser.add_argument('adm_no_from', type=int, help='Starting admission number')
parser.add_argument('adm_no_range', type=int, nargs='?', default=1, help='Range of admission number (default: 1)')
parser.add_argument('log_tc_data', type=int, nargs='?', default=0, help='To print student tc data in console (default: 0)')
args = parser.parse_args()

# extracting command line argument values
url = args.url
adm_no_from = args.adm_no_from
adm_no_range = args.adm_no_range - 1
log_tc_data = args.log_tc_data
admission_numbers = []

# validating the url
try:
  url = urlparse(url) # create a new URL object
  if not url.scheme or not url.netloc:
    raise ValueError # raise an error if the url is missing scheme or netloc
except ValueError:
  print('\x1b[31mPlease provide valid kendriya vidyalaya url. \x1b[33mExample - \x1b[32mpython script.py \x1b[4mhttps://no2udaipur.kvs.ac.in/\x1b[0m \x1b[32m3045701\x1b[0m')
  sys.exit(1) # exit the program with an error code

# validating the admission number
if adm_no_from <= 0:
  print('\x1b[31mPlease provide valid start admission numbers as arguments. \x1b[33mExample - \x1b[32mpython script.py https://no2udaipur.kvs.ac.in/ \x1b[4m3045701\x1b[0m \x1b[32m5\x1b[0m')
  sys.exit(1) # exit the program with an error code


headers = {
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1788.0  uacq',
  'Accept': 'application/json, text/javascript, */*; q=0.01',
  'Accept-Language': 'en-US,en;q=0.5',
  'Accept-Encoding': 'gzip, deflate, br',
  'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
  'X-Requested-With': 'XMLHttpRequest',
  'Origin': 'https://' + url.netloc,
  'Connection': 'keep-alive',
  'Referer': 'https://' + url.netloc + '/enrolment-statistics/tc-issued',
  'Cookie': 'has_js=1',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-origin',
  'sec-ch-ua-platform': '"macOS"',
  'sec-ch-ua': '"Edge";v="114", "Chromium";v="114", "Not=A?Brand";v="24"',
  'sec-ch-ua-mobile': '?0'
}

def process_data(table):
        rows = table.find_all('tr')
        headers = [th.text.strip() for th in rows[0].find_all('th')]
        data = []

        for row in rows[1:]:
            row_data = {}
            for index, cell in enumerate(row.find_all('td')):
                row_data[headers[index]] = cell.text.strip()
            data.append(row_data)

        print(json.dumps(data, indent=2))
    

# Define the payload for the request
payload = {}
def run():
    # imporintg required modules
    import requests
    from bs4 import BeautifulSoup
    import json

    for adm_no in range(adm_no_from, adm_no_from + adm_no_range + 1):
        payload = 'title=&field_date_value%5Bvalue%5D%5Byear%5D=&field_admission_number_value=&field_number_value_1='+str(adm_no)+'&view_name=enrolment_statistics&view_display_id=page&view_args=&view_path=enrolment-statistics%2Ftc-issued&view_base_path=enrolment-statistics%2Ftc-issued&view_dom_id=03b7df2fbfcb10aa42f22f4d157e14f1&pager_element=0&ajax_html_ids%5B%5D=block-utl-content-header-region-block&ajax_html_ids%5B%5D=header-navprt&ajax_html_ids%5B%5D=toggleSearch&ajax_html_ids%5B%5D=search-block-form&ajax_html_ids%5B%5D=edit-search-block-form--2&ajax_html_ids%5B%5D=edit-actions&ajax_html_ids%5B%5D=edit-submit&ajax_html_ids%5B%5D=toggleAccessibility&ajax_html_ids%5B%5D=toggleSocial&ajax_html_ids%5B%5D=block-views-school-header-section-block&ajax_html_ids%5B%5D=block-block-5&ajax_html_ids%5B%5D=fontSize&ajax_html_ids%5B%5D=main_menu&ajax_html_ids%5B%5D=block-nice-menus-3&ajax_html_ids%5B%5D=nav&ajax_html_ids%5B%5D=skipCont&ajax_html_ids%5B%5D=main-wrapper&ajax_html_ids%5B%5D=main&ajax_html_ids%5B%5D=breadcrumb&ajax_html_ids%5B%5D=content&ajax_html_ids%5B%5D=highlighted&ajax_html_ids%5B%5D=block-easy-breadcrumb-easy-breadcrumb&ajax_html_ids%5B%5D=content&ajax_html_ids%5B%5D=main-content&ajax_html_ids%5B%5D=page-title&ajax_html_ids%5B%5D=skipCont&ajax_html_ids%5B%5D=block-system-main&ajax_html_ids%5B%5D=views-exposed-form-enrolment-statistics-page&ajax_html_ids%5B%5D=edit-title-wrapper&ajax_html_ids%5B%5D=edit-title&ajax_html_ids%5B%5D=edit-field-date-value-wrapper&ajax_html_ids%5B%5D=edit-field-date-value-value-wrapper&ajax_html_ids%5B%5D=edit-field-date-value-value-inside-wrapper&ajax_html_ids%5B%5D=edit-field-date-value-value&ajax_html_ids%5B%5D=edit-field-date-value-value-year&ajax_html_ids%5B%5D=edit-field-admission-number-value-wrapper&ajax_html_ids%5B%5D=edit-field-admission-number-value&ajax_html_ids%5B%5D=edit-field-number-value-1-wrapper&ajax_html_ids%5B%5D=edit-field-number-value-1&ajax_html_ids%5B%5D=edit-submit-enrolment-statistics&ajax_html_ids%5B%5D=lightbox2-overlay&ajax_html_ids%5B%5D=lightbox&ajax_html_ids%5B%5D=outerImageContainer&ajax_html_ids%5B%5D=modalContainer&ajax_html_ids%5B%5D=frameContainer&ajax_html_ids%5B%5D=imageContainer&ajax_html_ids%5B%5D=lightboxImage&ajax_html_ids%5B%5D=hoverNav&ajax_html_ids%5B%5D=prevLink&ajax_html_ids%5B%5D=nextLink&ajax_html_ids%5B%5D=loading&ajax_html_ids%5B%5D=loadingLink&ajax_html_ids%5B%5D=imageDataContainer&ajax_html_ids%5B%5D=imageData&ajax_html_ids%5B%5D=imageDetails&ajax_html_ids%5B%5D=caption&ajax_html_ids%5B%5D=numberDisplay&ajax_html_ids%5B%5D=bottomNav&ajax_html_ids%5B%5D=frameHoverNav&ajax_html_ids%5B%5D=framePrevLink&ajax_html_ids%5B%5D=frameNextLink&ajax_html_ids%5B%5D=bottomNavClose&ajax_html_ids%5B%5D=bottomNavZoom&ajax_html_ids%5B%5D=bottomNavZoomOut&ajax_html_ids%5B%5D=lightshowPause&ajax_html_ids%5B%5D=lightshowPlay&ajax_page_state%5Btheme%5D=school&ajax_page_state%5Btheme_token%5D=pIky0bOT1hfmhWhGA4vNJMcRyCyKwJhXWIFrNSt9LZM&ajax_page_state%5Bcss%5D%5Bmodules%2Fsystem%2Fsystem.base.css%5D=1&ajax_page_state%5Bcss%5D%5Bmodules%2Fsystem%2Fsystem.menus.css%5D=1&ajax_page_state%5Bcss%5D%5Bmodules%2Fsystem%2Fsystem.messages.css%5D=1&ajax_page_state%5Bcss%5D%5Bmodules%2Fsystem%2Fsystem.theme.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fviews_slideshow%2Fviews_slideshow.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fsimplenews%2Fsimplenews.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fcalendar%2Fcss%2Fcalendar_multiday.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fdate%2Fdate_api%2Fdate.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fdate%2Fdate_popup%2Fthemes%2Fdatepicker.1.7.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fdate%2Fdate_repeat_field%2Fdate_repeat_field.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fdomain%2Fdomain_nav%2Fdomain_nav.css%5D=1&ajax_page_state%5Bcss%5D%5Bmodules%2Ffield%2Ftheme%2Ffield.css%5D=1&ajax_page_state%5Bcss%5D%5Bmodules%2Fnode%2Fnode.css%5D=1&ajax_page_state%5Bcss%5D%5Bmodules%2Fpoll%2Fpoll.css%5D=1&ajax_page_state%5Bcss%5D%5Bmodules%2Fsearch%2Fsearch.css%5D=1&ajax_page_state%5Bcss%5D%5Bmodules%2Fuser%2Fuser.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fviews%2Fcss%2Fviews.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fctools%2Fcss%2Fctools.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fall%2Fmodules%2Fcustom%2Fdomain_hirarchy%2Fdomain_hirarchy.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Flightbox2%2Fcss%2Flightbox.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fpanels%2Fcss%2Fpanels.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fall%2Fmodules%2Fcustom%2Futl_award%2Futl_award.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fall%2Fmodules%2Fcustom%2Futl_content%2Fassets%2Fcss%2Fbase.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fall%2Fmodules%2Fcustom%2Futl_content%2Fassets%2Fcss%2Ffont.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fall%2Fmodules%2Fcustom%2Futl_content%2Fassets%2Fcss%2Fflexslider.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fall%2Fmodules%2Fcustom%2Futl_content%2Fassets%2Fcss%2Fbase-responsive.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fall%2Fmodules%2Fcustom%2Futl_content%2Fassets%2Fcss%2Ffont-awesome.min.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fall%2Fmodules%2Fcustom%2Futl_content%2Fassets%2Fcss%2Fgrid.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fall%2Fmodules%2Fcustom%2Futl_content%2Fassets%2Fcss%2Futl-common.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fall%2Fmodules%2Fcustom%2Futl_permission%2Finclude%2Futl_permission.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fall%2Fmodules%2Fcustom%2Futl_popup%2Fpopup.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fnice_menus%2Fcss%2Fnice_menus.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fnice_menus%2Fcss%2Fnice_menus_default.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fviews_slideshow%2Fviews_slideshow_controls_text.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fviews_slideshow%2Fcontrib%2Fviews_slideshow_cycle%2Fviews_slideshow_cycle.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fresponsive_menus%2Fstyles%2FmeanMenu%2Fmeanmenu.min.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fall%2Fthemes%2Fschool%2Fcss%2Fbootstrap.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fall%2Fthemes%2Fschool%2Fcss%2Fanimate.min.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fall%2Fthemes%2Fschool%2Fcss%2Fanimation.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fall%2Fthemes%2Fschool%2Fcss%2Fsite.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fall%2Fthemes%2Fschool%2Fcss%2Fsite-responsive.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fall%2Fthemes%2Fschool%2Fcss%2Fprint.css%5D=1&ajax_page_state%5Bjs%5D%5B0%5D=1&ajax_page_state%5Bjs%5D%5B1%5D=1&ajax_page_state%5Bjs%5D%5B2%5D=1&ajax_page_state%5Bjs%5D%5B3%5D=1&ajax_page_state%5Bjs%5D%5B%2F%2Fcode.jquery.com%2Fjquery-2.2.4.min.js%5D=1&ajax_page_state%5Bjs%5D%5B%2F%2Fcode.jquery.com%2Fjquery-migrate-1.4.1.min.js%5D=1&ajax_page_state%5Bjs%5D%5Bmisc%2Fjquery-extend-3.4.0.js%5D=1&ajax_page_state%5Bjs%5D%5Bmisc%2Fjquery-html-prefilter-3.5.0-backport.js%5D=1&ajax_page_state%5Bjs%5D%5Bmisc%2Fjquery.once.js%5D=1&ajax_page_state%5Bjs%5D%5Bmisc%2Fdrupal.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fjquery_update%2Freplace%2Fui%2Fexternal%2Fjquery.cookie.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fclientside_validation%2Fjquery.form.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fnice_menus%2Fjs%2Fjquery.bgiframe.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fnice_menus%2Fjs%2Fjquery.hoverIntent.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fnice_menus%2Fjs%2Fsuperfish.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fnice_menus%2Fjs%2Fnice_menus.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fviews_slideshow%2Fjs%2Fviews_slideshow.js%5D=1&ajax_page_state%5Bjs%5D%5Bmisc%2Fajax.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fjquery_update%2Fjs%2Fjquery_update.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Flightbox2%2Fjs%2Flightbox.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fmodules%2Fcustom%2Futl_award%2Futl_award.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fmodules%2Fcustom%2Futl_content%2Fassets%2Fjs%2Ffont-size.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fmodules%2Fcustom%2Futl_content%2Fassets%2Fjs%2Fframework.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fmodules%2Fcustom%2Futl_content%2Fassets%2Fjs%2Fswithcer.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fviews%2Fjs%2Fbase.js%5D=1&ajax_page_state%5Bjs%5D%5Bmisc%2Fprogress.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fviews%2Fjs%2Fajax_view.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Flibraries%2Fjquery.cycle%2Fjquery.cycle.all.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fviews_slideshow%2Fcontrib%2Fviews_slideshow_cycle%2Fjs%2Fviews_slideshow_cycle.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fresponsive_menus%2Fstyles%2FmeanMenu%2Fjquery.meanmenu.min.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fresponsive_menus%2Fstyles%2FmeanMenu%2Fresponsive_menus_mean_menu.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fthemes%2Fschool%2Fjs%2Fjquery.flexslider.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fthemes%2Fschool%2Fjs%2Fsite.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fthemes%2Fschool%2Fjs%2FeasyResponsiveTabs.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fthemes%2Fschool%2Fjs%2Fwow.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fthemes%2Fschool%2Fjs%2Fjquery.marquee.js%5D=1&ajax_page_state%5Bjquery_version%5D=2.2'
        # payload['field_number_value_1'] = adm_no
        response = requests.request('POST', 'https://' + url.netloc + '/views/ajax', headers=headers, data=payload)
        html_data = json.loads(response.text)[2]['data']
        # html_data = json.loads(response.text)
        # pprint.pprint(html_data)

        # Check if table exist in html data or not
        soup = BeautifulSoup(html_data, 'html.parser')
        table = soup.find('table')

        if table:
            print('\x1b[32m\u2713 ' + str(adm_no)+ '\x1b[0m')
            if log_tc_data: process_data(table)
        else:
            print('\x1b[31m\u2717 ' + str(adm_no)+ '\x1b[0m')
            admission_numbers.append(adm_no)

run()

if len(admission_numbers):
    print(admission_numbers)
    with open('admission-numbers.txt', 'w') as f:
        for num in admission_numbers:
            f.write(str(num) + '\n')
