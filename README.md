# historical-dictionary
A google cloud server implementing a consistent dictionary with rollback feature

The app: http://historical-dictionary.appspot.com

The API:

Set 'a' to 12
```
/set?name=a&value=12
```

Get 'a' value
```
/get?name=a
```

Set 'a' value to null
```
/unset?name=a
```

Find out how many values are 12
```
/numequalto?value=12
```

Undo the last Set/Unset
```
/undo
```

Clean all
```
/end
```