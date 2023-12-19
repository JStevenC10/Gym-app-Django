# ADD ALL MESSAGE TO LIST
def add_list_messages(message_list, *args, **kwargs):
    for i in range(len(args)):
        message_list.append(args[i])
    return message_list

# MOTIVATION FOR GYM CLIENTS
MESSAGE1 = 'El éxito en el gym no es para aquellos que tienen talento, sino para aquellos que trabajan duro'
MESSAGE2 = 'No permitas que el miedo te detenga, sigue adelante'
MESSAGE3 = 'El éxito no se logra con suerte, se logra con esfuerzo y dedicación'
MESSAGE4 = 'Si no sudas, ¿estás realmente haciendo ejercicio?'
MESSAGE5 = 'La dificultad es lo que despierta al genio'
MESSAGE6 = 'No cuentes los dias, has que los dias cuenten'
MESSAGE7 = 'No busques el momento perfecto, solo busca el momento y hazlo perfecto'
MESSAGE8 = 'Todos nuestros sueños se pueden hacer realidad si tenemos el coraje de perseguirlos'
MESSAGE9 = 'Cuanto mejor te sientas contigo mismo, menos necesidad tendrás de buscar validación'
MESSAGE10 = 'El éxito en la vida no se mide por lo que logras sino por los obstáculos que superas'
MESSAGE11 = 'Soy mi propio experimento, soy mi propia obra de arte'
MESSAGE12 = 'Nunca agaches la cabeza. Siempre tenla bien alta. Mira al mundo directamente a los ojos'
MESSAGE13 = 'Aprende a apreciar lo increíble que eres'
MESSAGE14 = 'Quererse a uno mismo es el principio de un romance para toda la vida'
MESSAGE15 = 'Enamórate de ti, de la vida. Y luego de quien tú quieras'
MESSAGE16 = 'Nadie te detendrá cuando te des cuenta de lo poderosa, valiente y capaz que eres'
MESSAGE17 = 'Confía en ti mismo, de lo contrario, será difícil que los demás confíen en ti'
MESSAGE18 = 'Da siempre lo mejor de ti. Lo que siembres hoy dará su fruto mañana'
MESSAGE19 = 'Muchos bíceps pero para cuando la cara'
MESSAGE20 = 'cuando voy al Gym visto de negro porque es el funeral de mi yo gordo'
MESSAGE21 = 'Mientras tú me ignoras el entrenador del Gym me dice que cambiemos de posición'
MESSAGE22 = 'Si no estás dispuesto a sacrificar lo cotidiano, debes conformarte con lo ordinario'
MESSAGE23 = 'Nuestra tarea en la vida no es vencer a los demás, sino superarnos a nosotros mismos'
MESSAGE24 = 'No esperes el momento perfecto, has que el momento sea perfecto'
MESSAGE25 = 'El talento te abandona si no trabajas duro todos los días por lo que quieres conseguir'
MESSAGE26 = 'Te dejaron por otr@?, hoy toca corazon al fallo!'

# NO PAY MESSAGE
NOT_PAYED = "Sin mensualidad no hay mensaje! lo siento..."
NOT_PAYED_2 = "Primero paga, luego te motivo"

MOTIVATION = []
add_list_messages(MOTIVATION, MESSAGE1, MESSAGE2, MESSAGE3, MESSAGE4, MESSAGE5, MESSAGE6, \
                  MESSAGE7, MESSAGE8, MESSAGE9, MESSAGE10, MESSAGE11, MESSAGE12, MESSAGE13, \
                  MESSAGE14, MESSAGE15, MESSAGE16, MESSAGE17, MESSAGE18, MESSAGE19, MESSAGE20, \
                    MESSAGE21, MESSAGE22, MESSAGE23, MESSAGE24, MESSAGE25, MESSAGE26)
