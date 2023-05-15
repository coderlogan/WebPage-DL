from pywebcopy import save_website

save_website(
  url=input(),
  project_folder=r"./webpages/",
  project_name=input(),
  bypass_robots=True,
  debug=True,
  open_in_browser=False,
  delay=None,
  threaded=False
)