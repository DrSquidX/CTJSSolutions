import SquidWeb

server = SquidWeb.Website("localhost",80)
server.add_subdomain("/home","test.html")
server.add_subdomain("/calculator","Calculator.html")
server.add_subdomain("/calculator2","Area_per_calc.html")
server.start_server()

"""
# This is if you want to have a more simple way of adding subdomains.
import SquidWeb
server = SquidWeb.Website("localhost",80)
server.use_all_in_dir()
server.start_server()
"""
