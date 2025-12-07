import sh


class CUPSConnector:
    @staticmethod
    def get_printer_list():
    # Get list of CUPS printers via shell command `lpstat`
        try:
            sh_result = sh.lpstat("-e")
        except:

        destination_id_list = sh_result.split("\n")

        destination_list = []
        for destination_id in destination_id_list:
            destination_list.append(get_destination_info(destination_id))

        return destination_list

    def get_destination_info(destination_id: str) -> dict:
        # Get device_id
        
