def author(name='who is author'): 
	
	def decorator(func): 

		def wrapper(*args, **kwargs): 

			wrapper._author = name 

			return func(*args, **kwargs) 

		return wrapper 

	return decorator

