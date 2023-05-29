import tkinter as tk
from api_caller import get_data, load_data_from_last_run, refill_blacklist, save_data_from_last_run

root = tk.Tk()
root.geometry("1200x150")
root.title('Dynamics 365 API reverse engineering tool')

api_url = tk.StringVar()
api_url_label = tk.Label(root, text="API URL:")
api_url_entry = tk.Entry(root, textvariable=api_url, width=80)
api_url_label.grid(row=0, column=0)
api_url_entry.grid(row=0, column=1)

cookie = tk.StringVar()
cookie_label = tk.Label(root, text="Cookie:")
cookie_entry = tk.Entry(root, textvariable=cookie, width=80)
cookie_label.grid(row=1, column=0)
cookie_entry.grid(row=1, column=1)

entity_search_param = tk.StringVar()
search_param_label = tk.Label(root, text="Search Param:")
search_param_entry = tk.Entry(root, textvariable=entity_search_param, width=80)
search_param_label.grid(row=2, column=0)
search_param_entry.grid(row=2, column=1)

search_param_file = tk.StringVar()
search_param_file_label = tk.Label(
    root, text="Search param in every found entity:")
search_param_file_entry = tk.Entry(
    root, textvariable=search_param_file, width=80)
search_param_file_label.grid(row=3, column=0)
search_param_file_entry.grid(row=3, column=1)

thread_number = tk.IntVar()
thread_number_label = tk.Label(
    root, text="Threads:")
thread_number_entry = tk.Entry(
    root, textvariable=thread_number, width= 80)
thread_number_label.grid(row=4, column=0)
thread_number_entry.grid(row=4, column=1)


data = load_data_from_last_run('last_run_data.json')
api_url.set(data['api_url'])
cookie.set(data['cookie'])
entity_search_param.set(data['entity_search_param'])
search_param_file.set(data['search_param_file'])
thread_number.set(data['thread'])

def save():
    api_url_str = api_url.get()
    cookie_str = cookie.get()
    entity_search_param_str = entity_search_param.get()
    search_param_file_str = search_param_file.get()
    thread_number_int = thread_number.get()
    save_data_from_last_run(api_url_str, cookie_str,
                            entity_search_param_str, search_param_file_str, thread_number_int)


def proces_request_fetch_click():
    api_url_str = api_url.get()
    cookie_str = cookie.get()
    entity_search_param_str = entity_search_param.get()
    search_param_file_str = search_param_file.get()
    get_data(api_url_str, cookie_str,
             entity_search_param_str, search_param_file_str)


def process_request_blacklist_click():
    api_url_str = api_url.get()
    cookie_str = cookie.get()
    refill_blacklist(api_url_str, cookie_str)


fetch_button = tk.Button(
    root, text="Fetch", command=proces_request_fetch_click)
fetch_button.grid(row=0, column=2, padx=(0, 50))

refill_blacklist_button = tk.Button(
    root, text="Refill Blacklist", command=process_request_blacklist_click)
refill_blacklist_button.grid(row=1, column=2, padx=(20, 30))

root.mainloop()
save()
