"""
Este código se hizo en la carpeta donde está el entorno virtual y allí funciona debido a que en ese entorno tengo instalado Bokeh que es quien corre el scipt, por lo tanto,
al ejecutarlo acá globalmente donde no tengo instalado Bokeh, va arrojar error, sin embargo, pasé el código para acá
en la carpeta global porque el entorno virtual no lo voy a subir a git, pero es pa que quede como evidencia
Nota:

Para cuando lo vaya a ejecutar en el entorno virtual, primero debo ingresar a la carpeta graficado que es donde tengo el entorno virtual
luego, activar el entorno virtual con source env/Scripts/activate este comando es si lo hago desde git bash y por último correr el archivo como siempre:
python clase22_graficado_simple.py y ya ver el resultado en el navegador
"""
from bokeh.plotting import figure, output_file, show

if __name__ == '__main__':
    output_file('graficado_jose.html')
    fig = figure()
    
    total_vals = int(input("¿Cuántos valores quieres gráficar?: "))
    x_vals = list(range(total_vals))
    y_vals = []
    
    for i in x_vals:
        val = int(input(f'Valor y para {i}: '))
        y_vals.append(val)
        
    fig.line(x_vals, y_vals, line_width=2)
    show(fig)