# Mensaje para TI

Cópialo, reemplaza lo que está entre corchetes y envíalo. Es la única dependencia externa de la semana. Antes de enviarlo, desactiva en tu cuenta Pro el uso de los chats para entrenamiento (*Configuración › Privacidad*): el mensaje lo afirma.

---

**Asunto:** Piloto de una semana · conector Microsoft 365 de Claude · 1 usuario, solo lectura

Hola [nombre]:

Quiero pilotear durante una semana un asistente para la gerencia de manufactura. Lee mi correo, mi calendario y las transcripciones de Teams de mis reuniones para prepararme un resumen diario y las actas de reunión. Usa el conector oficial de Microsoft 365 de Anthropic (Claude).

**Lo que necesito**

1. **Consentimiento de administrador**, una sola vez, por un Global Administrator de Entra. Enlace oficial, reemplazando el ID del tenant:
   `https://login.microsoftonline.com/<ID-DEL-TENANT>/adminconsent?client_id=07c030f6-5743-41b7-ba00-0a6e85f37c17`
2. **Limitarlo a un usuario:** asignar la aplicación empresarial «M365 MCP Server for Claude» solo a mi usuario ([correo]).
3. **Dejarlo en solo lectura:** revocar `Mail.Send`, `ChatMessage.Send`, `ChannelMessage.Send` y `Chat.Create`. Si lo prefieren, también `Mail.ReadWrite`, `Calendars.ReadWrite`, `Files.ReadWrite.All` y `MailboxSettings.ReadWrite`.
4. **Acceso condicional:** si restringen por ubicación, permitir el rango de Anthropic `160.79.104.0/21`. La MFA sigue aplicando.

**Lo que conviene saber**

- Los permisos son delegados: el asistente ve solo lo que yo ya puedo ver, y respeta los permisos de SharePoint.
- El contenido se consulta en el momento de cada tarea, se envía a Claude para procesarlo y queda en el historial de mi cuenta de Claude (plan Pro, con el uso para entrenamiento desactivado).
- Se revoca en cualquier momento desde Entra.
- Guía de seguridad del fabricante: https://support.claude.com/en/articles/12684923-microsoft-365-connector-security-guide
- Configuración del conector: https://claude.com/docs/connectors/microsoft/365

Gracias,
[firma]
