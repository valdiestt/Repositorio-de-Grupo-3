# 1. IMPORTACIÓN DE CONFIGUACIÓN DE CLASE USUARIO
# =========================================================
from clase_user import Usuario

# Archivo: publicacion.py
class Publicacion:
    def __init__(self, autor, contenido):
        self.autor = autor
        self.contenido = contenido
        self.likes = 0
        self.comentarios = []

    def dar_like(self, usuario):
        self.likes += 1
        return True

    def comentar(self, usuario, texto):
        self.comentarios.append(f"@{usuario.obtener_nombre_usuario()}: {texto}")
        return True

    def __str__(self):
        return f"📝 '{self.contenido}' | ❤️ Likes: {self.likes} | 💬 Comentarios: {len(self.comentarios)}"
# =========================================================
# 2. FUNCIONES DEL MENÚ
# =========================================================
def mostrar_menu():
    print("\n" + "="*60)
    print("      SIMULACIÓN DE USUARIOS DE INSTAGRAM DEFINIDOS")
    print("="*60)
    print("1. Ver lista de usuarios registrados (User, Nombre, Correo)")
    print("2. Ver detalles completos de una cuenta (Perfil)")
    print("3. Gestión de Seguidores y Follows")
    print("4. Salir de la simulación")
    print("="*60)

def main():
    # Diccionario central para guardar los OBJETOS
    red_social = {}
    
    print("\n========== INFORMACIÓN DE REGISTRO PREVIO DE USUARIOS DEFINIDOS ==========")
    
    # Lista de datos definidos
    datos_usuarios = [
        ["valedies_1", "Valeria Guadalupe Diestra Vuelot", "valediestra@gmail.com"],
        ["gbustillos_2", "Gustavo Enrique Bustillos Semeler", "gbustillos@gmail.com"],
        ["stayci_3", "Stayci Marisol Ovalle Muñoz", "sovalle@gmail.com"],
        ["sebastian_4", "Sebastián Mauricio Díaz Pasache", "sdiaz@gmail.com"]
    ]

    # PROCESAMIENTO: Convertimos los datos crudos en objetos Usuario
    for datos in datos_usuarios:
        username = datos[0]
        nombre_completo = datos[1]
        correo = datos[2]
        
        # Imprimimos la lista cruda en consola
        print(datos)
        
        # Instanciamos la clase y la guardamos en el diccionario
        red_social[username] = Usuario(username, nombre_completo, correo)
        
    print("====================================================")
    print("✅ Todos los usuarios han sido convertidos a objetos exitosamente.")

    # =========================================================
    # 2. BUCLE DEL MENÚ INTERACTIVO
    # =========================================================
    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-4): ").strip()

        if opcion == '1':
            print("\n========== INFORMACIÓN DE CUENTA INSTAGRAM ==========")
            print("|===== User ====|========= Nombre Completo =========|======== Correo =======|")
            for usuario_definido in datos_usuarios:
                print(usuario_definido) 
                
        elif opcion == '2':
            print("\n--- BUSCAR PERFIL ---")
            buscar = input("Ingresa el @nombre_usuario que quieres revisar (ej. valedies_1): ").strip()
            
            if buscar in red_social:
                perfil = red_social[buscar]
                print(f"\n--- 👤 Perfil de @{buscar} ---")
                print(f"📛 Nombre Completo: {perfil.obtener_nombre_completo()}")
                print(f"📧 Correo: {perfil.obtener_correo()}")
                print(f"👥 Seguidores: {perfil.cantidad_seguidores()}")
                print(f"👣 Seguidos: {perfil.cantidad_seguidos()}")
                print(f"📸 Publicaciones: {perfil.cantidad_publicaciones()}")
                print(f"🌟 ¿Es Influencer?: {'Sí' if perfil.es_influencer() else 'No'}")
            else:
                print("❌ Ese usuario no existe en la simulación.")
                
        elif opcion == '3':
            # --- SUBMENÚ DE SEGUIDORES Y FOLLOWS ---
            while True:
                print("\n" + "-"*45)
                print("      OPCIÓN 3: GESTIÓN DE SEGUIDORES")
                print("-"*45)
                print("1. Simular un 'Follow' (Hacer que alguien siga a otro)")
                print("2. Ver a quién sigue un usuario (Seguidos)")
                print("3. Ver quién sigue a un usuario (Seguidores)")
                print("4. Volver al menú de opciones")
                print("-"*45)

                sub_opcion_3 = input("Elige una opción (1-4): ").strip()

                if sub_opcion_3 == '1':
                    print("\n--- SIMULACIÓN DE FOLLOW ---")
                    seguidor = input("¿Quién va a seguir? (Ingresa su @usuario): ").strip()
                    seguido = input("¿A quién va a seguir? (Ingresa su @usuario): ").strip()
                    
                    if seguidor in red_social and seguido in red_social:
                        exito = red_social[seguidor].seguir(red_social[seguido])
                        if exito:
                            print(f"✅ ¡Confirmado! @{seguidor} empezó a seguir a @{seguido}.")
                        else:
                            print("❌ No se pudo realizar la acción (Ya lo sigue o se eligió a sí mismo).")
                    else:
                        print("❌ Error: Verifica que escribiste bien los nombres de usuario.")

                elif sub_opcion_3 == '2':
                    print("\n--- LISTA DE SEGUIDOS ---")
                    buscar = input("Ingresa el @nombre_usuario: ").strip()
                    if buscar in red_social:
                        usuario_obj = red_social[buscar]
                        seguidos = usuario_obj.obtener_seguidos()
                        if len(seguidos) == 0:
                            print(f"👤 @{buscar} no sigue a nadie todavía.")
                        else:
                            print(f"👤 @{buscar} sigue a {len(seguidos)} cuenta(s):")
                            for cuenta in seguidos:
                                print(f"   - @{cuenta.obtener_nombre_usuario()}")
                    else:
                        print("❌ Ese usuario no existe.")

                elif sub_opcion_3 == '3':
                    print("\n--- LISTA DE SEGUIDORES ---")
                    buscar = input("Ingresa el @nombre_usuario: ").strip()
                    if buscar in red_social:
                        usuario_obj = red_social[buscar]
                        seguidores = usuario_obj.obtener_seguidores()
                        if len(seguidores) == 0:
                            print(f"👤 @{buscar} no tiene seguidores todavía.")
                        else:
                            print(f"👤 @{buscar} es seguido por {len(seguidores)} cuenta(s):")
                            for cuenta in seguidores:
                                print(f"   - @{cuenta.obtener_nombre_usuario()}")
                    else:
                        print("❌ Ese usuario no existe.")

                elif sub_opcion_3 == '4':
                    print("↩️ Volviendo al menú principal...")
                    break  # Sale del submenú y regresa al menú de opciones

                else:
                    print("❌ Opción no válida. Ingresa un número del 1 al 4.")

        elif opcion == '4':
            print("\nSaliendo de la simulación del Grupo 3... ¡Hasta luego!")
            break
            
        else:
            print("\n❌ Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()