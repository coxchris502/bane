from bane.bruteforce.utils import *

class admin_panel_finder:
    __slots__ = ["stop", "finish", "result", "logs"]

    def done(self):
        return self.finish

    """
   this function use a list of possible admin panel links with different extensions: php, asp, aspx, js, /, cfm, cgi, brf and html.
   
   ext: (set by default to: 'php') to define the link's extention.

   usage:

  >>>import bane
  >>>bane.admin_panel_finder('http://www.example.com',ext='php',timeout=7)

  >>>bane.admin_panel_finder('http://www.example.com',ext='aspx',timeout=5)
 """

    def __init__(
        self,
        u,
        logs=True, 
        threads_daemon=True,
        user_agent=None,
        cookie=None,
        ext="php",
        timeout=10,
        headers={},
        http_proxies=None,
        socks4_proxies=None,
        socks5_proxies=None
        ):
        """
        This function searches for potential admin panel URLs on a website using a predefined list of extensions.
        
        Parameters:
        - u (str): The target website URL.
        - logs (bool): Enable or disable logging (default is True).
        - threads_daemon (bool): Set thread as daemon (default is True).
        - user_agent (str): Custom User-Agent header for requests.
        - cookie (str): Custom cookies to include in requests.
        - ext (str): Extension to use for URLs (default is 'php').
        - timeout (int): Request timeout in seconds (default is 10).
        - headers (dict): Additional HTTP headers to include.
        - http_proxies (list): List of HTTP proxies to use.
        - socks4_proxies (list): List of SOCKS4 proxies to use.
        - socks5_proxies (list): List of SOCKS5 proxies to use.
        """
        proxies=get_requests_proxies_from_parameters(http_proxies=http_proxies,socks4_proxies=socks4_proxies,socks5_proxies=socks5_proxies)
        self.logs = logs
        self.stop = False
        self.finish = False
        self.result = {}
        t = threading.Thread(
            target=self.crack,
            args=(
                u,
                timeout,
                logs,
                ext,
                user_agent,
                cookie,
                proxies,
                headers,
            ),
        )
        t.daemon = threads_daemon
        t.start()

    def crack(
        self,
        u,
        timeout,
        logs,
        ext,
        user_agent,
        cookie,
        proxies,
        headers
    ):
        links = []
        ext = ext.strip()
        if ext.lower() == "php":
            links = phpl
        elif ext.lower() == "asp":
            links = aspl
        elif ext.lower() == "aspx":
            links = aspxl
        elif ext.lower() == "js":
            links = jsl
        elif ext == "/":
            links = slashl
        elif ext.lower() == "cfm":
            links = cfml
        elif ext.lower() == "cgi":
            links = cgil
        elif ext.lower() == "brf":
            links = brfl
        elif ext.lower() == "html":
            links = htmll
        k = []
        for i in links:
            if self.stop == True:
                break
            try:
                proxy = random.choice(proxies)
                if user_agent:
                    us = user_agent
                else:
                    us = random.choice(ua)
                hed = {"User-Agent": us}
                if cookie:
                    hed.update({"Cookie": cookie})
                hed.update(headers)
                if u[len(u) - 1] == "/":
                    u = u[0 : len(u) - 1]
                g = u + i
                if logs == True:
                    print("[*]Trying:", g)
                r = requests.Session().get(
                    g,
                    headers=hed,
                    allow_redirects=False,
                    proxies=proxy,
                    timeout=timeout,
                    verify=False,
                )
                if r.status_code == requests.Session().codes.ok:
                    if logs == True:
                        print("[+]FOUND!!!")
                    k.append(g)
                else:
                    if logs == True:
                        print("[-]failed")
            except KeyboardInterrupt:
                break
            except Exception as e:
                if logs == True:
                    print("[-]Failed")
        self.result = {u: k}
        self.finish = True

