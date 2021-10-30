"""contains functions for converting these news files to an html file"""
import webbrowser
import time
from rss_package import log


@log.log_decorator
def convert_to_html(news, settings, path):
    with open(path, "w", encoding="utf-8") as html_file:
        for item in news:
            html_item = f''' 
                        <a href="{item["link"]}" class="list-group-item list-group-item-action d-flex gap-3 py-3" \\ 
                        aria-current="true">
                            <img src="{item["image"]}" alt="twbs" width="150" class= flex-shrink-0">
                            <div class="d-flex gap-2 w-100 justify-content-between">
                            <div>
                                <p class="h5">{item["title"]}</p>
                                <p class="mb-0 opacity-75">{item["description"]}</p>
    
                            </div>
                            <small class="opacity-50 text-nowrap">{item["pubdate"]}</small>
                            </div>
                        </a>
                        '''

            html_file.write(html_item)
        footer = '''
                    </div>
                    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"\\
                         integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" \\
                             crossorigin="anonymous"></script>
                    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js" \\
                        integrity="sha384-IQsoLXl5PILFhosVNubq5LC7Qb9DXgDA9i+tQ8Zj3iwWAwPtgFTxbJ8NT4GN1R8p"\\
                             crossorigin="anonymous"></script>
                    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.min.js" \\ 
                    integrity="sha384-cVKIPhGWiC2Al4u+LWgxfKTRIcfu0JTxR+EQDz/bgldoEyl4H0zUF0QKbrJ0EcQF"\\
                         crossorigin="anonymous"></script>
                    </body>
                    </html>
                    '''

        html_file.write(footer)
        print("Html file created successfully!!")

        time.sleep(2)
        webbrowser.open_new_tab(path)