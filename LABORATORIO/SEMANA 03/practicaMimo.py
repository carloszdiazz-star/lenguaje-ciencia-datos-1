"""Lorde olvidó su contraseña y está usando un programa para restaurarla. El programa verifica si su nueva contraseña es diferente de la antigua. También hace que Lorde ingrese la nueva contraseña dos veces para asegurarse de que esté escrita correctamente. iTerminemos ese programa!
1. Usa el operador de desigualdad en compare_old_new para mostrar que las contraseñas no son iguales.
2. Asegúrate de que new_password coincida con
repeat_new_password."""
old_password = "hello123"
new_password = "goodbye321"
repeat_new_password = "goodbye321"


comparacion = new_password != old_password
comparacion_repeticion = new_password == repeat_new_password



print(f"Is new password different from old? {comparacion}")
print(f"Has new password been correctly repeated? {comparacion_repeticion}")

