from django.core.exceptions import ValidationError

class PasswordHasAlpha:
    def validate(self,passw,user=None):
        if not any(char.isalpha() for char in passw):
            raise ValidationError('il doit avoir une lettre',code='no_char_password')
    def get_help_text(self):
        return 'il doit avoir au moins un caractère dans '
    
class PasswordHasNumeric:
    def validate(self,passw,user=None):
        if not any(char.isdigit() for char in passw):
            raise ValidationError('il doit avoir au moins un nombre numérique dans votre mot de passe',code='no_numeric_password')
    def get_help_text(self):
        return 'il doit avoir au moins un chiffre dans le mot de passe'