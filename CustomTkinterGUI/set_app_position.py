def set_app_position(app):
	app.update_idletasks()
	w = app.geometry()
	print([w, app.winfo_width(), app.winfo_height()])
	screen_w, screen_h = app.winfo_screenwidth(), app.winfo_screenheight() # размер дисплея
	app.update_idletasks()
	w = app.geometry()
	print([w, app.winfo_width(), app.winfo_height()])
	center_w, center_h = screen_w // 2, screen_h // 2 # середина дисплея
	app.update_idletasks()
	w = app.geometry()
	print([w, app.winfo_width(), app.winfo_height()])
	app_w, app_h = app.winfo_screenwidth() - 100, app.winfo_screenheight() - 100 # размер окна
	app.update_idletasks()
	w = app.geometry()
	print([w, app.winfo_width(), app.winfo_height()])
	app_center_w, app_center_h = app_w // 2, int(app_h // 1.855) # середина окна
	app.update_idletasks()
	w = app.geometry()
	print([w, app.winfo_width(), app.winfo_height()])
	app.geometry(f'{app_w}x{app_h}+{center_w - app_center_w}+{center_h - app_center_h}')
	app.update_idletasks()
	w = app.geometry()
	print([w, app.winfo_width(), app.winfo_height()])