# Reglas para trabajar en este repo

Este repo es el taller del segundo cerebro del gerente de manufactura: aquí se escriben y prueban las skills, las plantillas y los scripts. El sistema en operación corre en Claude (tareas programadas en la nube y la app), no en Claude Code. El plan y las fases están en `PLAN.md`.

1. **Español** en todo: documentos, código, commits y conversación.
2. **Por fases.** `PLAN.md` manda. No se avanza de fase sin aprobación explícita del usuario.
3. **Los datos reales nunca entran al repo.** Correos, actas y nombres de clientes, proveedores o personas viven en Microsoft 365 y en OneDrive (`Cerebro/`). Aquí solo hay skills, plantillas, pruebas y decisiones. Un ejemplo dentro de una skill es inventado y lo dice.
4. **Rigor en toda salida del sistema:**
   - cada cifra con su fuente;
   - dato separado de inferencia;
   - nunca rellenar lo que falta;
   - **cero no es calma**: toda salida declara cuánto leyó, para que un día tranquilo no se confunda con una fuente que no se pudo leer;
   - **el modelo no suma**: los números salen de la fuente o de un script.
5. **Skills:**
   - Una tarea por skill y `SKILL.md` corto.
   - La versión vive en el cuerpo del `SKILL.md` y sube con cada cambio.
   - Antes de entregar: `python3 scripts/empaquetar_skills.py --probar` y después `python3 scripts/empaquetar_skills.py`. Los ZIP salen en `dist/`, que no se versiona.
   - Todo cambio de skill se prueba contra `pruebas/` antes de subirlo a la cuenta.
6. **Decisiones** con su alternativa descartada y sus fuentes, en `docs/decisiones/AAAA-MM-DD-<tema>.md`.
7. **Commits** con Conventional Commits (`feat:`, `fix:`, `docs:`, `chore:`).
