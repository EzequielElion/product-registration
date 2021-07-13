from sqlite3.dbapi2 import Cursor
from PyQt5 import uic,QtWidgets
import DataBaser
from reportlab.pdfgen import canvas
import sqlite3

numero_id = 0

def editar_dados():
    global numero_id
    linha = Product.tableWidget.currentRow()
    
    
    DataBaser.cursor.execute("""
    SELECT id FROM Cadastro
    
    """)
    dadosLidos = DataBaser.cursor.fetchall()
    valor_id = dadosLidos[linha][0]
    DataBaser.cursor.execute("SELECT * FROM Cadastro WHERE id=" + str(valor_id))
    produto = DataBaser.cursor.fetchall()
    TelaEditar.show()

    numero_id = valor_id

    TelaEditar.lineEdit_5.setText(str(produto[0][0]))
    TelaEditar.lineEdit.setText(str(produto[0][1]))
    TelaEditar.lineEdit_2.setText(str(produto[0][2]))
    TelaEditar.lineEdit_3.setText(str(produto[0][3]))
    TelaEditar.lineEdit_4.setText(str(produto[0][4]))
   

def salvarEdit():
    global numero_id
    codigo = TelaEditar.lineEdit.text()
    descricao = TelaEditar.lineEdit_3.text()
    preco = TelaEditar.lineEdit_2.text()
    categoria = TelaEditar.lineEdit_4.text()
    
    conn = sqlite3.connect('Data.db')

    cursor = conn.cursor()
    DataBaser.cursor.execute("UPDATE Cadastro SET codigo = '{}', preco = '{}', descricao = '{}', categoria = '{}' WHERE id = {}".format(codigo,descricao,preco,categoria,numero_id))

    TelaEditar.close()
    Product.close()
    mostrarDados()


def excluir_dados():
    linha = Product.tableWidget.currentRow()
    Product.tableWidget.removeRow(linha)
    
    DataBaser.cursor.execute("""
    SELECT id FROM Cadastro
    
    """)
    dadosLidos = DataBaser.cursor.fetchall()
    valor_id = dadosLidos[linha][0]
    DataBaser.cursor.execute("DELETE FROM Cadastro WHERE id=" + str(valor_id))
   
    print(valor_id)


def gerar_pdf():
    print("gerar pdf")
    DataBaser.cursor.execute("""
    SELECT * FROM Cadastro
    """)
    dadosLidos = DataBaser.cursor.fetchall()
    y=0
    pdf = canvas.Canvas("cadastro_produtos.pdf")
    pdf.setFont("Times-Bold", 25)
    pdf.drawString(200,800, "Produtos cadastrados:")
    pdf.setFont("Times-Bold", 18)

    pdf.drawString(10,750, "ID")
    pdf.drawString(110,750, "CODIGO")
    pdf.drawString(210,750, "PREÇO")
    pdf.drawString(310,750, "PRODUTO")
    pdf.drawString(410,750, "CATEGORIA")

    for i in range(0, len(dadosLidos)):
        y = y + 50 
        pdf.drawString(10,750 - y, str(dadosLidos[i][0]))
        pdf.drawString(110,750 - y, str(dadosLidos[i][1]))
        pdf.drawString(210,750 - y, str(dadosLidos[i][2]))
        pdf.drawString(310,750 - y, str(dadosLidos[i][3]))
        pdf.drawString(410,750 - y, str(dadosLidos[i][4]))
        
    pdf.save()
    print("PDF FOI GERADO COM SUCESSO!!!")



def funcao_principal():
    codigo = ProductReg.lineEdit.text()
    preco = ProductReg.lineEdit_2.text()
    descricao = ProductReg.lineEdit_3.text()

    categoria=""

    if ProductReg.radioButton.isChecked() :
        print("Categoria alimentos foi selecionada")
    
        categoria ="Alimentos"

    elif ProductReg.radioButton_2.isChecked() :
            
        categoria="Limpeza"

        print("Castegoria limpeza foi selecionada")
    else :
        print("Categoria higiene foi selecionada")    

        categoria="Higiene"


    print("Código", codigo)
    print("Descrição", preco)
    print("Preço", descricao)

    DataBaser.cursor.execute("""
    INSERT INTO cadastro(codigo, descricao, preco, categoria) VALUES(?, ?, ?, ?)
            
    """,(codigo, descricao, preco, categoria))
    DataBaser.conn.commit()

    ProductReg.lineEdit.setText("")
    ProductReg.lineEdit_2.setText("")
    ProductReg.lineEdit_3.setText("")

def mostrarDados():
    Product.show()

    DataBaser.cursor.execute("""
    SELECT * FROM Cadastro
    """)
    dadosLidos = DataBaser.cursor.fetchall()
    

    Product.tableWidget.setRowCount(len(dadosLidos))
    Product.tableWidget.setColumnCount(5)

    for i in range(0, len(dadosLidos)):
        for j in range(0, 5):
            Product.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dadosLidos[i][j])))






    
app=QtWidgets.QApplication([])
ProductReg=uic.loadUi("ProductReg.ui")
Product=uic.loadUi("Product.ui")
TelaEditar=uic.loadUi("MenuEdit.ui")
ProductReg.pushButton.clicked.connect(funcao_principal)
ProductReg.pushButton_2.clicked.connect(mostrarDados)
Product.pushButton.clicked.connect(gerar_pdf)
Product.pushButton_2.clicked.connect(excluir_dados)
Product.pushButton_3.clicked.connect(editar_dados)
TelaEditar.pushButton.clicked.connect(salvarEdit)

ProductReg.show()
app.exec()
