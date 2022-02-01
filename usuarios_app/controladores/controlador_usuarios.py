from flask import Flask, render_template,session,redirect,request
from usuarios_app import app
from usuarios_app.modelos.modelo_usuarios import Usuario

@app.route('/',methods=['GET'])
def paginaInicio():
    if 'confirmar' not in session:
        return render_template('agregar.html')
    return render_template('agregar.html')

@app.route('/agregar',methods=['POST'])
def agregarUsuario():
    nuevoUsuario = {
        "nombre" : request.form["nombre"],
        "apellido" : request.form["apellido"],
        "email" : request.form["email"]
    }
    if nuevoUsuario['nombre']=='':
        return redirect('/')
    else: 
        session['confirmar']=1
        resultado = Usuario.agregarUsuario(nuevoUsuario)
        return redirect('/leer')

@app.route('/leer',methods=['GET'])
def mostrarUsuarios():
    listaDeUsuarios = Usuario.obtenerListaUsarios()
    return render_template('leer.html',listaDeUsuarios=listaDeUsuarios)