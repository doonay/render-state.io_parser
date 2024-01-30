'''
Для демонстрации нужно в базе sqlite3
создать таблицу test_crud
с полями item_id (integer autoincrement) и name (текст)
'''

import flet as ft
from flet import UserControl, Page
import sqlite3

conn = sqlite3.connect("flet_test_crud.db", check_same_thread=False)
cur = conn.cursor()

class MyClass(ft.UserControl):
	def __init__(self):
		super().__init__()
		# LIST DATA
		self.alldata = ft.Column()
		self.addData = ft.TextField(label="add new data")
		self.editData = ft.TextField(label="add new data")

	#PROSES DELETE DATA
	def prosesDelete(self, x, b):
		# X AND B IS PARAM FOR FUNCTION
		cur.execute("delete from test_crud where item_id = ?", [x])
		conn.commit()
		# CLOSE YOU ALWRT DIALOG
		b.open = False
		# CALL rerenderAll FUNCTION AGAIN FOR REFRESH THE DATA
		self.alldata.controls.clear()
		self.renderAll()
		self.page.update()

	#PROSES EDIT DATA
	def prosesEdit(self, a, x, b):
		print("a is", a)
		print("x is", x)
		print("b is", b)
		cur.execute("update test_crud SET name = ? where item_id = ?", (x, a))
		conn.commit()
		# CLOSE YOU ALWRT DIALOG
		b.open = False
		# CALL rerenderAll FUNCTION AGAIN FOR REFRESH THE DATA
		self.alldata.controls.clear()
		self.renderAll()
		self.page.update()

	def OpenYOuAction(self, e):
		# GET ID FROM DATA
		id_edit = e.control.subtitle.value
		# EDIT TEXTEDIT TO VALUE NAME FROM LISTTITTLE
		self.editData.value = e.control.title.value
		self.update()

		# OPEN ALERT DIALOG
		alert_dialog = ft.AlertDialog(
			title=ft.Text(f"Edit id {id_edit}"),
			content=self.editData,
			# BUTTON ACTIONS
			actions = [
				# DELETE DATA
				ft.ElevatedButton(
					"Delete data",
					color="ehite",
					bgcolor="red",
					on_click=lambda e:self.prosesDelete(id_edit, alert_dialog)
				),
				# EDIT BUTTON
				ft.TextButton(
					"Save Edit",
					on_click=lambda e:self.prosesEdit(
						id_edit,
						self.editData.value,
						alert_dialog)
				)
			],
			actions_alignment="spaceBetween"
		)
		self.page.dialog = alert_dialog
		alert_dialog.open = True
		# UPDATE DATA
		self.page.update()

	#RENDER TO PUSH TO WIDGET FETCH
	def renderAll(self):
		cur.execute("select * from test_crud")
		conn.commit()
		mydata = cur.fetchall()
		for x in mydata:
			self. alldata.controls.append(
				ft.ListTile(
					# GET NAME
					title=ft.Text(x[1]),
					# GET ID
					subtitle=ft.Text(x[0]),
					on_click = self.OpenYOuAction
				)
			)
		self.update()

	#LIFECYCLE FOR CALL RENDERALL
	def did_mount(self):
		self.renderAll()

	def funaddNew(self, e):
		cur.execute("insert into test_crud (name) values (?)", [self.addData.value])
		conn.commit()
		# CLEAR DATA AND CALL AGAIN
		self.alldata.controls.clear()
		#self.editData.value=None
		self.addData.value=None
		self.renderAll()
		self.page.update()


	def build(self):
		return ft.Column([
			ft.Text("CRUD SQLITE", size=30),
			self.addData,
			ft.ElevatedButton("Add new data",
			on_click=self.funaddNew),
			#SEE ALLDATA
			self.alldata
		])

def main(page:Page):
	page.update()
	myclass = MyClass()
	page.add(myclass)

ft.app(target=main, assets_dir="assets")