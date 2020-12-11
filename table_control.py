
from type_weight_setup import type_weight_setup
from key_weight_setup import key_weight_setup
from key_act_setup import key_act_setup
from inv_act_setup import inv_act_setup
from inv_weight_setup import inv_weight_setup
from type_setup import type_setup
from chord_db_drop import tab_drop

def table_control(on_or_off):

    def tab_setup():  # establishes write portion of function
        key_weight_setup()
        type_setup()
        key_act_setup()
        type_weight_setup()
        inv_weight_setup()
        inv_act_setup()
    def drop(): # establishes drop portion of function
        tab_drop("key_act")
        tab_drop("key_weight")
        tab_drop("type_weight")
        tab_drop("k_act")
        tab_drop("inv_act")
        tab_drop("inv_weight")
    
    # controls if function writes or drops
    if on_or_off == "on":
        tab_setup()
    elif on_or_off == "off":
        drop()
    
