#!/usr/bin/env python3
# import flywheel_gear_toolkit

import flywheel
import logging


# def main(gtk_context: flywheel_gear_toolkit.GearToolkitContext):
def main(context):

    # print(dir(gtk_context))
    # print(f"Using gtkcontext: {gtk_context.config.get('qc_type')}")

    # qc_tag="ReadyforImageQC"
    # file_to_tag = gtk_context.get_input("file_to_qc")
    # gtk_context.update_file_metadata(file_to_tag,tags=[qc_tag])

    config = context.config # from the gear context, get the config settings
    print(config)
    # tag_to_add = config['qc_type']





if __name__ == "__main__": 
    # with flywheel_gear_toolkit.GearToolkitContext() as gtk_context:
    #     # Setup basic logging
    #     gtk_context.init_logging()
    #     # Log the configuration for this job
    #     gtk_context.log_config()

    #     main(gtk_context)
    # Initialize logging and set its level  
    logging.basicConfig()  
    log = logging.getLogger()  
    log.setLevel(logging.INFO)

    context = flywheel.GearContext() # Get the gear context  

    main(context)