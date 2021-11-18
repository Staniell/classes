
#Running it directly
if __name__ == "__main__":
    import mathematics

#Importing from outside
else:
    from subjects import mathematics

x = mathematics.Arithmetic(2,4)
print(x.Add())
