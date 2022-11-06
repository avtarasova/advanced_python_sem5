import random

def connection():
	import random
	connections = [establish_connection(True) for i in range(10)]
	connections.append(establish_connection(False))
	connections.append(establish_connection(False))
	while len(connections):
		conn = random.choice(connections)
		try:
			yield next(conn)
		except StopIteration:
			del connections[connections.index(conn)]



def establish_connection(auth=True):
	id = f"{random.randint(0,100000000):010}"
	if auth:
		yield f"auth {id}"
		yield from connect_user(id)
	if auth:
		yield f"disconnect {id}"



def connect_user(username):

	filename = f'{username}.txt'
	with open(filename, 'a') as file:
		yield from write_to_file(file, username)



def write_to_file(f_obj, identity):

	for i in range(random.randint(10, 20)):
		yield f_obj.write(f"{identity} message{i} \n")


for i in connection():
	print(i)



# for i in establish_connection(auth=False):
# 	print(i)