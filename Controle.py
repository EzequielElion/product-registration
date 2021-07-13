from PyQt5 import uic,QtWidgets
import DataBaser


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
ProductReg.pushButton.clicked.connect(funcao_principal)
ProductReg.pushButton_2.clicked.connect(mostrarDados)
ProductReg.show()
app.exec()
