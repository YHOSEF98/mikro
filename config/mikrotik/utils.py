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


def deshabilitar_servicio(host, username, password, port, target_ip):
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
        rule_params = {
            'chain': 'forward',  # La cadena de reenvío
            'src-address': target_ip, # ip del cliente
            'action': 'drop',  # Acción para bloquear el tráfico
            'name': 'Suspendido_por_pago' # nombre de la regla
        }

        # Obtener el recurso de colas
        queues_resource = api.get_resource('/ip/firewall/filter')
        queue_tag = "suspendido"
        # Crear la cola usando el método add()
        queues_resource.add(tag=queue_tag, **rule_params)

        print("Servicio deshabiitado")
    except Exception as e:
        print("No se pudo establecer la conexión:", str(e))


def habilitar_servicio(host, username, password, port, target_ip):
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
        #buscar la regla para esa ip
        queues_resource = api.get_resource('/ip/firewall/filter')
        existing_rule = None
        for rule in queues_resource.get():
            if rule.get('name') == 'Suspendido_por_pago' and rule.get('action') == 'drop':
                existing_rule = rule
                break

        if existing_rule:
            existing_rule['action'] = 'accept'
            queues_resource.set(id=existing_rule['id'], **existing_rule)

        else:
            rule_params = {
                'chain': 'forward',  # La cadena de reenvío
                'src-address': target_ip,  # Reemplaza con la dirección IP del cliente
                'action': 'accept',  # Acción para Autorizar  el tráfico
                'name': 'ips_autorizadas'
            }

            # Crear la cola usando el método add()
            queues_resource.add(**rule_params)
            print("regla creada con exito")

            print("Servicio habiitado")
    except Exception as e:
        print("No se pudo establecer la conexión:", str(e))

def crear_regla_corte(host, username, password, port):
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
        
        # Definir el nombre de la regla
        rule_name = 'Mora'
        
        # Obtener el recurso de reglas de firewall
        nat_resource = api.get_resource('/ip/firewall/nat')
        
        nat_params_tcp = {
                'chain': 'dstnat',  # La cadena de reenvío
                'src-address-list': rule_name,  # IP del cliente
                'action': 'redirect',  # Acción para bloquear el tráfico
                'comment': 'Manager - Suspension de ips (TCP)',  # Nombre de la regla
                'to-ports': '999',
                'protocol': 'tcp',
                'dst-port': '!8291'
            }
        nat_params_udp = {
                'chain': 'dstnat',  # La cadena de reenvío
                'src-address-list': rule_name,  # IP del cliente
                'action': 'redirect',  # Acción para bloquear el tráfico
                'comment': 'Manager - Suspension de ips (UDP)',  # Nombre de la regla
                'to-ports': '999',
                'protocol': 'udp',
                'dst-port': '!8291,53'
            }
        # Verificar si ya existe una regla con el mismo nombre y acción
        nats = nat_resource.get()
        existing_nat_tcp = None
        existing_nat_udp = None
        
        for nat in nats:
            if nat.get('src-address-list') == rule_name and nat.get('protocol') == 'tcp':
                existing_nat_tcp = nat
                print("regla tcp existente")
                break 
        
        if existing_nat_tcp:
            # Eliminar la regla NAT existente
            nat_resource.remove(id=existing_nat_tcp['id'])
            print(f"Regla NAT eliminada")
            nat_resource.add(**nat_params_tcp)
            print("regla nat tcp creada")
        else:
            nat_resource.add(**nat_params_tcp)
            print("regla nat creada tcp")

        for nat in nats:
            if nat.get('src-address-list') == rule_name and nat.get('protocol') == 'udp':
                existing_nat_udp = nat
                print("regla udp existente")
                break

        if existing_nat_udp:
            # Eliminar la regla NAT existente
            nat_resource.remove(id=existing_nat_udp['id'])
            print(f"Regla NAT eliminada")
            nat_resource.add(**nat_params_udp)
            print("regla nat udp creada")
        else:
            nat_resource.add(**nat_params_udp)
            print("regla nat creada udp")

        #CREAR REGLA FILTER
        filter_resource = api.get_resource('/ip/firewall/filter')
        filter_params = {
                'chain': 'forward',  # La cadena de reenvío
                'src-address-list': rule_name,  # Nombre de la lista
                'action': 'drop',  # Acción para bloquear el tráfico
                'comment': 'filtro de corte de servicio en mora',  # Nombre de la regla
            }
        # Verificar si ya existe una regla con el mismo nombre y acción
        filters = filter_resource.get()
        existing_filter = None
        
        for filter in filters:
            if nat.get('src-address-list') == rule_name:
                existing_filter = filter
                print("regla tcp existente")
                break 
        
        if existing_filter:
            # Eliminar la regla NAT existente
            filter_resource.remove(id=existing_filter['id'])
            print(f"Filtro NAT eliminado")
            filter_resource.add(**filter_params)
            print("filtro nap creado")
        else:
            filter_resource.add(**filter_params)
            print("filtro nap creado")
    except Exception as e:
        print("No se pudo establecer la conexión o realizar la operación:", str(e))