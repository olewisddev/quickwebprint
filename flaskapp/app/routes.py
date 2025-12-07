from cups_connector import CUPSConnector
import jsonify


@app.route("/api/printers", ["GET"])
def get_printer_list():
# Get list of available printers
    printer_list = []

    try:
        printer_list = CUPSConnector.get_printer_list()
        return jsonify({"printer_list": printer_list}), 200
    except Exception as e:
        print(f"ERROR: {str(e)}")
        return jsonify({"error": "Failed to retrieve printer list."}), 500


