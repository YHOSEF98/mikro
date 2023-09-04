#from .models import *
import ssl
import routeros_api


def create_queue(host, username, password, port, queue_name, target_ip, max_limit):
    try:
        connection = routeros_api.RouterOsApiPool(
            host=host,
            username=username,
            password=password,
            plaintext_login=True,
            port=port,
            use_ssl=False,
            ssl_verify=True,
            ssl_verify_hostname=False,
            ssl_context=None,
        )
        api = connection.get_api()
        #print("Conexión exitosa")

        # Definir los parámetros para crear la cola
        queue_params = {
            'name': queue_name,
            'target': target_ip,
            'max-limit': max_limit,
        }

        # Obtener el recurso de colas
        queues_resource = api.get_resource('/queue/simple')

        # Crear la cola usando el método add()
        queues_resource.add(**queue_params)

        print("Cola creada exitosamente")
    except Exception as e:
        print("No se pudo establecer la conexión:", str(e))



def eliminar_queue(host, username, password, port, queue_name):
    try:
        connection = routeros_api.RouterOsApiPool(
            host=host,
            username=username,
            password=password,
            plaintext_login=True,
            port=port,
            use_ssl=False,
            ssl_verify=True,
            ssl_verify_hostname=False,
            ssl_context=None,
        )
        api = connection.get_api()
        print("Conexión exitosa")

        # Obtener el recurso de colas
        queues_resource = api.get_resource('/queue/simple')

        # Obtener todas las colas
        queues = queues_resource.get()
        #print(queues)

        # Buscar la cola por nombre
        queue_to_delete = None
        for queue in queues:
            if queue['name'] == queue_name:
                queue_to_delete = queue
                print(queue_to_delete)
                break

        if queue_to_delete:
            # Eliminar la cola utilizando el método remove()
            queues_resource.remove(id=queue_to_delete['id'])
            print("cola eliminada")
            return True
        else:
            print(f"No se encontró una cola con el nombre '{queue_name}'")

    except Exception as e:
        print("No se pudo establecer la conexión o eliminar la cola:", str(e))


def editar_queue(host, username, password, port, queue_name, new_name, target_ip, max_limit):
    try:
        connection = routeros_api.RouterOsApiPool(
            host=host,
            username=username,
            password=password,
            plaintext_login=True,
            port=port,
            use_ssl=False,
            ssl_verify=True,
            ssl_verify_hostname=False,
            ssl_context=None,
        )
        api = connection.get_api()
        print("Conexión exitosa")

        # Obtener el recurso de colas
        queues_resource = api.get_resource('/queue/simple')

        # Obtener todas las colas
        queues = queues_resource.get()
        # print(queues)

        # Buscar la cola por nombre
        queue_to_edit = None
        for queue in queues:
            if queue['name'] == queue_name:
                queue_to_edit = queue
                # print(queue_to_edit)
                break
        
        queue_params = {
            'name': new_name,
            'target': target_ip,
            'max-limit': max_limit,
        }

        if queue_to_edit:
            queues_resource.set(id=queue_to_edit['id'], **queue_params)
            print("cola Actualizada")
            return True
        else:
            print(f"No se encontró una cola con el nombre '{queue_name}'")

    except Exception as e:
        print("No se pudo establecer la conexión o actualizar la cola:", str(e))