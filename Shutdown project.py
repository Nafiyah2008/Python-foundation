def shutdown(response):
 if response == 'yes':
  return 'Shutting down'
 elif response == 'no' :
  return 'Abort shutdown'
 else:
  return 'Sorry'
n = input("Do you want to shut program?")
print(shutdown(n))
 

