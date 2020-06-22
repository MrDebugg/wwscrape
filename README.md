# wwscrape

wwscarpe is a Tool that crawls all links from a website and checks the crawled links if they exist or if they are false positives or if they are returning the status code 200.

Usage:

      python wwscrape.py <URL>

Example:

      python wwscrape.py https://test.com

Output:


      __  _  ____  _  ________ ________________  ______   ____
      \ \/ \/ /\ \/ \/ /  ___// ___\_  __ \__  \ \____ \_/ __ \
       \     /  \     /\___ \  \___|  | \// __ \|  |_> >  ___/
        \/\_/    \/\_//____  >\___  >__|  (____  /   __/ \___  >
                           \/     \/           \/|__|        \/
                                      by Mrdebugger

      [09:55:15] starting

      [*] Extracing all urls directories and files


      https://test.com/search=test
      https://test.com/secret/files.html
      https://test.com/shop/products/list,html
      https://test.com/shop/
      https://test.com/shop/products/

      [09:58:15] Done
