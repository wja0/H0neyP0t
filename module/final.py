import ids_ap as ids
import model_check as mdc
import client as srv
import os
from requests import get
#import requests

if __name__ == "__main__":
    host_ip = get("https://api.ipify.org").text
    attack = False
    c_socket = srv.connection_server()
    scan_model, atk_model = mdc.model_init()
    
    while(True):
        traffic_df = ids.scan_data()
        
        if os.fork() == 0:
            #err = srv.check_server(c_socket)
            
            
            #if err:
            #    print("Can't connect to secure server!")

            attack, bad_traffic = mdc.check_attack(traffic_df, scan_model, atk_model, host_ip)
            
            if attack:
                #infrom_usr()
                srv.send_to_server(c_socket, bad_traffic)
            
            exit(0)#child process down
        
        print("restart scan data")
                
        
        
            
