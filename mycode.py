from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector


class Hospital:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")

        self.PatientId= StringVar()
        self.PatientName= StringVar()
        self.Age= StringVar()
        self.DateOfBirth= StringVar()
        self.Gender= StringVar()
        self.PhoneNumber= StringVar()
        self.HomeAddress= StringVar()
        self.BloodPressure= StringVar()
        self.Temperature= StringVar()
        self.BloodOxygenLevel= StringVar()
        self.AppointmentId= StringVar()
        self.AppointmentDate= StringVar()
        self.DoctorId= StringVar()
        self.DoctorName= StringVar()
        self.DiagnosisDetails= StringVar()
        self.BillingId= StringVar()
        self.Amount= StringVar()
        self.Payment= StringVar()

        lbltitle = Label(self.root, bd=20, relief=RIDGE, text="HOSPITAL MANAGEMENT SYSTEM", fg="DarkGreen", bg="white",
                         font=("times new roman", 50, "bold"))
        lbltitle.pack(side=TOP, fill=X)

        Dataframe = Frame(self.root, bd=20, relief=RIDGE)
        Dataframe.place(x=0, y=130, width=1540, height=400)

        DataframeLeft = LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10, font=("times new roman", 12, "bold"),
                                   text="Patient Information")
        DataframeLeft.place(x=0, y=5, width=980, height=350)

        DataframeRight = LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10, font=("times new roman", 12, "bold"),
                                    text="Report")
        DataframeRight.place(x=990, y=5, width=460, height=350)

        Buttonframe = Frame(self.root, bd=20, relief=RIDGE)
        Buttonframe.place(x=0, y=530, width=1540, height=70)

        Detailsframe = Frame(self.root, bd=20, relief=RIDGE)
        Detailsframe.place(x=0, y=600, width=1540, height=190)


        Label(DataframeLeft, font=("arial", 12, "bold"), text="Patient ID:", padx=2).grid(row=0, column=0, sticky=W)
        Entry(DataframeLeft, font=("arial", 13, "bold"), width=35, textvariable=self.PatientId).grid(row=0, column=1)

        Label(DataframeLeft, font=("arial", 12, "bold"), text="Patient Name:", padx=2).grid(row=1, column=0, sticky=W)
        Entry(DataframeLeft, font=("arial", 13, "bold"), width=35, textvariable=self.PatientName).grid(row=1, column=1)

        Label(DataframeLeft, font=("arial", 12, "bold"), text="Age:", padx=2, pady=4).grid(row=2, column=0, sticky=W)
        Entry(DataframeLeft, font=("arial", 13, "bold"), width=35, textvariable=self.Age).grid(row=2, column=1)

        Label(DataframeLeft, font=("arial", 12, "bold"), text="Date of Birth:", padx=2, pady=6).grid(row=3, column=0,
                                                                                                     sticky=W)
        Entry(DataframeLeft, font=("arial", 13, "bold"), width=35, textvariable=self.DateOfBirth).grid(row=3,
                                                                                                           column=1)

        Label(DataframeLeft, font=("arial", 12, "bold"), text="Gender:", padx=2, pady=6).grid(row=4, column=0, sticky=W)
        Entry(DataframeLeft, font=("arial", 13, "bold"), width=35, textvariable=self.Gender).grid(row=4, column=1)

        Label(DataframeLeft, font=("arial", 12, "bold"), text="Phone Number:", padx=2, pady=6).grid(row=5, column=0,
                                                                                                  sticky=W)
        Entry(DataframeLeft, font=("arial", 13, "bold"), width=35, textvariable=self.PhoneNumber).grid(row=5, column=1)

        Label(DataframeLeft, font=("arial", 12, "bold"), text="Home Address:", padx=2, pady=6).grid(row=6, column=0,
                                                                                                sticky=W)
        Entry(DataframeLeft, font=("arial", 13, "bold"), width=35, textvariable=self.HomeAddress).grid(row=6, column=1)

        Label(DataframeLeft, font=("arial", 12, "bold"), text="Blood Pressure:", padx=2, pady=6).grid(row=7, column=0,
                                                                                                  sticky=W)
        Entry(DataframeLeft, font=("arial", 13, "bold"), width=35, textvariable=self.BloodPressure).grid(row=7, column=1)

        Label(DataframeLeft, font=("arial", 12, "bold"), text="Temperature:", padx=2, pady=6).grid(row=8, column=0,
                                                                                                   sticky=W)
        Entry(DataframeLeft, font=("arial", 13, "bold"), width=35, textvariable=self.Temperature).grid(row=8, column=1)

        Label(DataframeLeft, font=("arial", 12, "bold"), text="Blood Oxygen Level:", padx=2, pady=6).grid(row=0,
                                                                                                           column=2,
                                                                                                           sticky=W)
        Entry(DataframeLeft, font=("arial", 13, "bold"), width=35, textvariable=self.BloodOxygenLevel).grid(row=0,
                                                                                                              column=3)

        Label(DataframeLeft, font=("arial", 12, "bold"), text="Appointment ID:", padx=2, pady=6).grid(row=1, column=2,
                                                                                                      sticky=W)
        Entry(DataframeLeft, font=("arial", 13, "bold"), width=35, textvariable=self.AppointmentId).grid(row=1,
                                                                                                               column=3)

        Label(DataframeLeft, font=("arial", 12, "bold"), text="Appointment Date:", padx=2, pady=6).grid(row=2, column=2,
                                                                                                      sticky=W)
        Entry(DataframeLeft, font=("arial", 12, "bold"), width=35, textvariable=self.AppointmentDate).grid(row=2,
                                                                                                         column=3)

        Label(DataframeLeft, font=("arial", 12, "bold"), text="Doctor ID:", padx=2, pady=6).grid(row=3, column=2,
                                                                                                  sticky=W)
        Entry(DataframeLeft, font=("arial", 12, "bold"), width=35, textvariable=self.DoctorId).grid(row=3,
                                                                                                              column=3)

        Label(DataframeLeft, font=("arial", 12, "bold"), text="Doctor Name:", padx=2, pady=6).grid(row=4, column=2,
                                                                                                  sticky=W)
        Entry(DataframeLeft, font=("arial", 12, "bold"), width=35, textvariable=self.DoctorName).grid(row=4, column=3)

        Label(DataframeLeft, font=("arial", 12, "bold"), text="Diagnosis Details:", padx=2, pady=6).grid(row=5, column=2,
                                                                                                  sticky=W)
        Entry(DataframeLeft, font=("arial", 12, "bold"), width=35, textvariable=self.DiagnosisDetails).grid(row=5, column=3)

        Label(DataframeLeft, font=("arial", 12, "bold"), text="Billing ID:", padx=2, pady=6).grid(row=6, column=2,
                                                                                                    sticky=W)
        Entry(DataframeLeft, font=("arial", 12, "bold"), width=35, textvariable=self.BillingId).grid(row=6, column=3)

        Label(DataframeLeft, font=("arial", 12, "bold"), text="Total Amount Due:", padx=2, pady=6).grid(row=7, column=2, sticky=W)
        Entry(DataframeLeft, font=("arial", 12, "bold"), width=35, textvariable=self.Amount).grid(row=7, column=3)

        Label(DataframeLeft, font=("arial", 12, "bold"), text="Payment Status:", padx=2, pady=6).grid(row=8, column=2,
                                                                                                       sticky=W)
        Entry(DataframeLeft, font=("arial", 12, "bold"), width=35, textvariable=self.Payment).grid(row=8,
                                                                                                          column=3)

        self.txtPrescription = Text(DataframeRight, font=("arial", 12, "bold"), width=45, height=16, padx=2, pady=6)
        self.txtPrescription.grid(row=0, column=0)

        btnPrescription = Button(Buttonframe, text="Prescription", command=self.iPrescription, bg="green", fg="white",
                                 font=("times new roman", 12, "bold"), width=26, padx=2, pady=6)
        btnPrescription.grid(row=0, column=0)

        btnPrescriptionData = Button(Buttonframe, text="Prescription Data", command=self.iPrescriptionData, bg="green",
                                     fg="white", font=("times new roman", 12, "bold"), width=26, padx=2, pady=6)
        btnPrescriptionData.grid(row=0, column=1)

        btnUpdate = Button(Buttonframe, text="Update", command=self.update, bg="green", fg="white",
                           font=("times new roman", 12, "bold"), width=26, padx=2, pady=6)
        btnUpdate.grid(row=0, column=2)

        btnDelete = Button(Buttonframe, text="Delete", command=self.delete, bg="green", fg="white",
                           font=("times new roman", 12, "bold"), width=26, padx=2, pady=6)
        btnDelete.grid(row=0, column=3)

        btnClear = Button(Buttonframe, text="Clear", command=self.clear, bg="green", fg="white",
                          font=("times new roman", 12, "bold"), width=26, padx=2, pady=6)
        btnClear.grid(row=0, column=4)

        btnExit = Button(Buttonframe, text="Exit", bg="green", fg="white", font=("times new roman", 12, "bold"),
                         width=26, padx=2, pady=6, command=self.iExit)
        btnExit.grid(row=0, column=5)

        scroll_x = ttk.Scrollbar(Detailsframe, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Detailsframe, orient=VERTICAL)

        self.hospital_table = ttk.Treeview(Detailsframe,column=("PatientId","PatientName","Age","DateOfBirth","Gender","PhoneNumber","HomeAddress","BloodPressure","Temperature","BloodOxygenLevel","AppointmentId","AppointmentDate","DoctorId","DoctorName","DiagnosisDetails","BillingId","Amount","Payment"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.hospital_table.xview)
        scroll_y.config(command=self.hospital_table.yview)

        self.hospital_table.heading("PatientId", text="Patient ID")
        self.hospital_table.heading("PatientName", text="Patient Name")
        self.hospital_table.heading("Age", text="Age")
        self.hospital_table.heading("DateOfBirth", text="Date of Birth")
        self.hospital_table.heading("Gender", text="Gender")
        self.hospital_table.heading("PhoneNumber", text="Phone Number")
        self.hospital_table.heading("HomeAddress", text="Home Address")
        self.hospital_table.heading("BloodPressure", text="Blood Pressure")
        self.hospital_table.heading("Temperature", text="Temperature")
        self.hospital_table.heading("BloodOxygenLevel", text="Blood Oxygen Level")
        self.hospital_table.heading("AppointmentId", text="Appointment ID")
        self.hospital_table.heading("AppointmentDate", text="Appointment Date")
        self.hospital_table.heading("DoctorId", text="Doctor ID")
        self.hospital_table.heading("DoctorName", text="Doctor Name")
        self.hospital_table.heading("DiagnosisDetails", text="Diagnosis Details")
        self.hospital_table.heading("BillingId", text="Billing ID")
        self.hospital_table.heading("Amount", text="Total Amount Due")
        self.hospital_table.heading("Payment", text="Payment Status")

        self.hospital_table["show"] = "headings"

        self.hospital_table.column("PatientId", width=100)
        self.hospital_table.column("PatientName", width=100)
        self.hospital_table.column("Age", width=100)
        self.hospital_table.column("DateOfBirth", width=100)
        self.hospital_table.column("Gender", width=100)
        self.hospital_table.column("PhoneNumber", width=100)
        self.hospital_table.column("HomeAddress", width=100)
        self.hospital_table.column("BloodPressure", width=100)
        self.hospital_table.column("Temperature", width=100)
        self.hospital_table.column("BloodOxygenLevel", width=100)
        self.hospital_table.column("AppointmentId", width=100)
        self.hospital_table.column("AppointmentDate", width=100)
        self.hospital_table.column("DoctorId", width=100)
        self.hospital_table.column("DoctorName", width=100)
        self.hospital_table.column("DiagnosisDetails", width=100)
        self.hospital_table.column("BillingId", width=100)
        self.hospital_table.column("Amount", width=100)
        self.hospital_table.column("Payment", width=100)

        self.hospital_table.pack(fill=BOTH, expand=1)
        self.hospital_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def iPrescriptionData(self):
        if self.PatientId .get() == "" or self.PatientName.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="Hemanath", database="myhospital")
            my_cursor = conn.cursor()
            my_cursor.execute("insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                self.PatientId.get(),
                self.PatientName.get(),
                self.Age.get(),
                self.DateOfBirth.get(),
                self.Gender.get(),
                self.PhoneNumber.get(),
                self.HomeAddress.get(),
                self.BloodPressure.get(),
                self.Temperature.get(),
                self.BloodOxygenLevel.get(),
                self.AppointmentId.get(),
                self.AppointmentDate.get(),
                self.DoctorId.get(),
                self.DoctorName.get(),
                self.DiagnosisDetails.get(),
                self.BillingId.get(),
                self.Amount.get(),
                self.Payment.get()
            ))

            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success", "Record has been inserted")

    def update(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Hemanath", database="myhospital")
        my_cursor = conn.cursor()
        my_cursor.execute("update hospital set PatientName=%s,Age=%s,DateOfBirth=%s,Gender=%s,PhoneNumber=%s,HomeAddress=%s,BloodPressure=%s,Temperature=%s,BloodOxygenLevel=%s,AppointmentId=%s,AppointmentDate=%s,DoctorId=%s,DoctorName=%s,DiagnosisDetails=%s,BillingId=%s,Amount=%s,Payment=%s where PatientId=%s",
            (
                    self.PatientName.get(),
                    self.Age.get(),
                    self.DateOfBirth.get(),
                    self.Gender.get(),
                    self.PhoneNumber.get(),
                    self.HomeAddress.get(),
                    self.BloodPressure.get(),
                    self.Temperature.get(),
                    self.BloodOxygenLevel.get(),
                    self.AppointmentId.get(),
                    self.AppointmentDate.get(),
                    self.DoctorId.get(),
                    self.DoctorName.get(),
                    self.DiagnosisDetails.get(),
                    self.BillingId.get(),
                    self.Amount.get(),
                    self.Payment.get(),
                    self.PatientId.get()
            ))
        conn.commit()
        conn.close()
        self.fetch_data()
        messagebox.showinfo("Success", "Record has been updated")

    def iExit(self):
        iExit = messagebox.askyesno("Hospital Management System", "Do you want to exit?")
        if iExit > 0:
            self.root.destroy()
            return

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Hemanath", database="myhospital")
        my_cursor = conn.cursor()
        my_cursor.execute("Select * from hospital")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                self.hospital_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    def get_cursor(self, event=""):
        cursor_row = self.hospital_table.focus()
        content = self.hospital_table.item(cursor_row)
        row = content["values"]
        self.PatientId.set(row[0])
        self.PatientName.set(row[1])
        self.Age.set(row[2])
        self.DateOfBirth.set(row[3])
        self.Gender.set(row[4])
        self.PhoneNumber.set(row[5])
        self.HomeAddress.set(row[6])
        self.BloodPressure.set(row[7])
        self.Temperature.set(row[8])
        self.BloodOxygenLevel.set(row[9])
        self.AppointmentId.set(row[10])
        self.AppointmentDate.set(row[11])
        self.DoctorId.set(row[12])
        self.DoctorName.set(row[13])
        self.DiagnosisDetails.set(row[14])
        self.BillingId.set(row[15])
        self.Amount.set(row[16])
        self.Payment.set(row[17])


    def iPrescription(self):
        self.txtPrescription.insert(END, "Patient ID:\t\t\t" + self.PatientId .get() + "\n")
        self.txtPrescription.insert(END, "Patient Name:\t\t\t" + self.PatientName.get() + "\n")
        self.txtPrescription.insert(END, "Age:\t\t\t" + self.Age.get() + "\n")
        self.txtPrescription.insert(END, "Date of Birth:\t\t\t" + self.DateOfBirth.get() + "\n")
        self.txtPrescription.insert(END, "Gender:\t\t\t" + self.Gender.get() + "\n")
        self.txtPrescription.insert(END, "Phone Number:\t\t\t" + self.PhoneNumber.get() + "\n")
        self.txtPrescription.insert(END, "Home Address:\t\t\t" + self.HomeAddress.get() + "\n")
        self.txtPrescription.insert(END, "Blood Pressure:\t\t\t" + self.BloodPressure.get() + "\n")
        self.txtPrescription.insert(END, "Temperature:\t\t\t" + self.Temperature.get() + "\n")
        self.txtPrescription.insert(END, "Blood Oxygen Level:\t\t\t" + self.BloodOxygenLevel.get() + "\n")
        self.txtPrescription.insert(END, "Appointment ID:\t\t\t" + self.AppointmentId.get() + "\n")
        self.txtPrescription.insert(END, "Appointment Date :\t\t\t" + self.AppointmentDate.get() + "\n")
        self.txtPrescription.insert(END, "Doctor ID :\t\t\t" + self.DoctorId.get() + "\n")
        self.txtPrescription.insert(END, "Doctor Name:\t\t\t" + self.DoctorName.get() + "\n")
        self.txtPrescription.insert(END, "Diagnosis Details:\t\t\t" + self.DiagnosisDetails.get() + "\n")
        self.txtPrescription.insert(END, "Billing ID:\t\t\t" + self.BillingId.get() + "\n")
        self.txtPrescription.insert(END, "Total Amount Due:\t\t\t" + self.Amount.get() + "\n")
        self.txtPrescription.insert(END, "Payment Status:\t\t\t" + self.Payment.get() + "\n")

    def delete(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Hemanath", database="myhospital")
        my_cursor = conn.cursor()
        query = "delete from hospital where PatientId=%s"
        value = (self.PatientId.get(),)
        my_cursor.execute(query, value)
        conn.commit()
        conn.close()
        self.fetch_data()
        messagebox.showinfo("Success", "Record has been deleted")

    def clear(self):
        self.PatientId.set("")
        self.PatientName.set("")
        self.Age.set("")
        self.DateOfBirth.set("")
        self.Gender.set("")
        self.PhoneNumber.set("")
        self.HomeAddress.set("")
        self.BloodPressure.set("")
        self.Temperature.set("")
        self.BloodOxygenLevel.set("")
        self.AppointmentId.set("")
        self.AppointmentDate.set("")
        self.DoctorId.set("")
        self.DoctorName.set("")
        self.DiagnosisDetails.set("")
        self.BillingId.set("")
        self.Amount.set("")
        self.Payment.set("")
        self.txtPrescription.delete("1.0", END)


if __name__ == "__main__":
    root = Tk()
    obj = Hospital(root)
    root.mainloop()
