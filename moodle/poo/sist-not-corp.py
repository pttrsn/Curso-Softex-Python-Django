class Usuario:
    def __init__(self, nome: str, email: str):
        self.nome = nome
        self.__email = None
        self.email = email

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, novo_email: str) -> None:
        if isinstance(novo_email, str) and "@" in novo_email:
            self.__email = novo_email
        else:
            print("Erro: email inválido. Deve conter '@'.")


class CanalEnvio:
    def enviar(self, mensagem: str) -> None:
        raise NotImplementedError("Subclasses devem implementar 'enviar'.")


class Email(CanalEnvio):
    def enviar(self, mensagem: str) -> None:
        print(f"📧 Enviando para servidor de email: {mensagem}")


class SMS(CanalEnvio):
    def enviar(self, mensagem: str) -> None:
        print(f"📱 Enviando para operadora telefônica: {mensagem}")


class SistemaAlerta:
    def __init__(self, usuario: Usuario, canal: CanalEnvio):
        self.usuario = usuario
        self.canal = canal

    def disparar(self, texto: str) -> None:
        mensagem_personalizada = f"Olá, {self.usuario.nome}! {texto}"
        self.canal.enviar(mensagem_personalizada)


if __name__ == "__main__":
    usuario = Usuario("Maria", "maria@example.com")
    print("Email atual:", usuario.email)
    usuario.email = "email_invalido"
    print("Email após tentativa inválida:", usuario.email)
    usuario.email = "maria@empresa.com"
    print("Email após atualização válida:", usuario.email)

    canal_email = Email()
    sistema_email = SistemaAlerta(usuario, canal_email)
    sistema_email.disparar("Seu pagamento foi aprovado.")

    canal_sms = SMS()
    sistema_sms = SistemaAlerta(usuario, canal_sms)
    sistema_sms.disparar("Servidor caiu. Equipe já está investigando.")