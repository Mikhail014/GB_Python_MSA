import interface
import data

data.all_data_import()
interface.select_role()

while data.is_active_program:
    interface.action_mode(data.selected_role)
