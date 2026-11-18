<div align="center">

# CUENTA PAYPAL TEMPORAL EN UNA SOCIEDAD CIVIL

### Hasta la obtención del NIF / CIF definitivo

---

**Documento orientativo de procedimiento fiscal, documental y operativo**

**Proyecto Icarus**

---

| | |
|:--|:--|
| **Ámbito** | España · Sociedad Civil (SC) · PayPal (Europa) · Agencia Tributaria (AEAT) |
| **Tipo de documento** | Guía práctica de cumplimiento y justificación de cobros |
| **Versión** | 1.1 |
| **Fecha** | Noviembre 2026 |
| **Estado** | Orientativo — no vinculante |

---

*Este documento analiza si una sociedad civil puede operar con PayPal antes de disponer del NIF definitivo, cómo hacerlo de forma ordenada y cómo justificar la cuenta y los ingresos del periodo temporal.*

</div>

---

> **Aviso importante.** Esta guía es orientativa. **No constituye asesoramiento jurídico, fiscal ni financiero vinculante.** Las condiciones de PayPal, la normativa tributaria y los criterios de verificación KYC/AML pueden cambiar. Antes de operar con cobros reales, conviene contrastar el caso concreto con un asesor fiscal/mercantil y, si hace falta, con soporte de PayPal Business.

---

## Índice

1. [Resumen ejecutivo](#1-resumen-ejecutivo)
2. [Marco conceptual: qué es una Sociedad Civil a estos efectos](#2-marco-conceptual-qué-es-una-sociedad-civil-a-estos-efectos)
   - [2.1. Naturaleza mercantil/civil](#21-naturaleza-mercantilcivil)
   - [2.2. NIF vs “CIF”](#22-nif-vs-cif)
   - [2.3. Obligación clave antes de cobrar](#23-obligación-clave-antes-de-cobrar)
3. [NIF provisional y NIF definitivo (AEAT)](#3-nif-provisional-y-nif-definitivo-aeat)
   - [3.1. NIF provisional](#31-nif-provisional)
   - [3.2. NIF definitivo](#32-nif-definitivo)
   - [3.3. Plazos y riesgos del provisional](#33-plazos-y-riesgos-del-provisional)
   - [3.4. Implicación para PayPal](#34-implicación-para-paypal)
4. [Qué exige PayPal (España / EEE)](#4-qué-exige-paypal-españa--eee)
   - [4.1. Tipos de cuenta](#41-tipos-de-cuenta)
   - [4.2. Datos habituales al crear Business](#42-datos-habituales-al-crear-business)
   - [4.3. Documentación de verificación](#43-documentación-de-verificación-orientativa)
   - [4.4. ¿PayPal acepta NIF provisional?](#44-paypal-acepta-nif-provisional)
5. [Escenarios posibles (de mejor a peor)](#5-escenarios-posibles-de-mejor-a-peor)
   - [Escenario A — Recomendado](#escenario-a--recomendado-nif-provisional--paypal-business-de-la-sc)
   - [Escenario B — Puente de emergencia](#escenario-b--puente-de-emergencia-cuenta-business-de-un-socio-autónomo-o-personal-convertida-con-mandato-interno)
   - [Escenario C — Evitar](#escenario-c--evitar-cuenta-personal-de-la-empresa-sin-alta-sin-facturas-sin-rastro)
6. [Procedimiento detallado recomendado](#6-procedimiento-detallado-recomendado-paso-a-paso)
   - [Fase 0 — Preparación societaria](#fase-0--preparación-societaria)
   - [Fase 1 — Alta censal y NIF provisional](#fase-1--alta-censal-y-nif-provisional)
   - [Fase 2 — Cuenta bancaria](#fase-2--cuenta-bancaria)
   - [Fase 3 — Alta PayPal Business](#fase-3--alta-paypal-business)
   - [Fase 4 — Operativa temporal](#fase-4--operativa-temporal-con-nif-provisional)
   - [Fase 5 — Paso a NIF definitivo](#fase-5--paso-a-nif-definitivo)
7. [Cómo justificar la cuenta y los ingresos “temporales”](#7-cómo-justificar-la-cuenta-y-los-ingresos-temporales)
   - [7.1. Frente a PayPal](#71-frente-a-paypal-titularidad-y-uso)
   - [7.2. Frente a Hacienda](#72-frente-a-hacienda-naturaleza-y-atribución-del-ingreso)
   - [7.3. Frente a los socios](#73-frente-a-los-socios-gobierno-interno)
   - [7.4. Paquete mínimo por ingreso](#74-paquete-mínimo-de-justificación-por-cada-ingreso)
   - [7.5. Contabilidad del periodo provisional](#75-contabilidad-práctica-del-periodo-provisional)
8. [Caso específico: recaudación de fondos / proyecto](#8-caso-específico-recaudación-de-fondos--proyecto-p-ej-landing-de-crowdfunding-interno)
9. [Checklist operativo](#9-checklist-operativo)
10. [Riesgos principales y cómo mitigarlos](#10-riesgos-principales-y-cómo-mitigarlos)
11. [Preguntas frecuentes](#11-preguntas-frecuentes)
12. [Modelo breve de mandato interno](#12-modelo-breve-de-mandato-interno-puente-de-emergencia)
13. [Conclusión práctica](#13-conclusión-práctica)
14. [Referencias útiles](#14-referencias-útiles-consulta)
15. [Anexo: mapa de decisión](#15-anexo-mapa-de-decisión)
16. [Problemas legales y financieros que puede ocasionar](#16-problemas-legales-y-financieros-que-puede-ocasionar)
    - [16.1. Problemas legales y regulatorios](#161-problemas-legales-y-regulatorios)
    - [16.2. Problemas fiscales](#162-problemas-fiscales)
    - [16.3. Problemas financieros y de tesorería](#163-problemas-financieros-y-de-tesorería)
    - [16.4. Problemas entre socios y frente a terceros](#164-problemas-entre-socios-y-frente-a-terceros)
    - [16.5. Escenarios de daño acumulado](#165-escenarios-de-daño-acumulado)
    - [16.6. Señales de alarma](#166-señales-de-alarma-parar-y-regularizar)
    - [16.7. Coste de prevenir vs coste de remediar](#167-coste-de-prevenir-frente-a-coste-de-remediar)

---

## 1. Resumen ejecutivo

| Pregunta | Respuesta corta |
|---|---|
| ¿Puede una SC crear una cuenta PayPal **Business a nombre de la entidad** sin NIF? | **En la práctica, no de forma estable.** PayPal exige identificación fiscal y documentación de la entidad. Sin NIF (provisional o definitivo) la verificación suele fallar o la cuenta queda limitada. |
| ¿Existe un “PayPal temporal oficial” mientras llega el CIF/NIF definitivo? | **No.** PayPal no ofrece un producto llamado “cuenta temporal”. Lo que sí existe en España es el **NIF provisional** de la AEAT, que permite operar y, a menudo, abrir/verificar la cuenta Business. |
| ¿Se puede cobrar “mientras tanto” con la PayPal personal de un socio? | **Solo como puente de emergencia, con riesgos altos** (condiciones de uso, atribución incorrecta de ingresos, mezcla de patrimonios, problemas de justificación ante Hacienda y ante socios). Si se usa, debe documentarse y migrarse de inmediato. |
| ¿Qué es lo correcto? | **1)** Constituir/documentar la SC → **2)** solicitar **NIF provisional** (modelo 036) **antes de cobrar** → **3)** abrir PayPal Business con ese NIF → **4)** justificar cada ingreso → **5)** cuando llegue el NIF definitivo, actualizar AEAT y PayPal. |

**Conclusión operativa:** la solución limpia no es “una PayPal temporal sin CIF”, sino **acelerar el NIF provisional** y, con él, abrir la cuenta Business a nombre de la SC. Si aún no hay NIF provisional, **no se deberían percibir cobros** por actividad de la entidad.

---

## 2. Marco conceptual: qué es una Sociedad Civil a estos efectos

### 2.1. Naturaleza mercantil/civil

Una **sociedad civil** es un contrato de colaboración entre dos o más personas que ponen en común dinero, bienes o industria para un fin común (Código Civil). A efectos prácticos:

- Puede tener o no personalidad jurídica según cómo se constituya y publique.
- **No suele inscribirse en el Registro Mercantil** (salvo supuestos concretos).
- Fiscalmente, si **no tiene objeto mercantil**, suele tributar en **régimen de atribución de rentas** (no como Impuesto sobre Sociedades).
- Si tiene **objeto mercantil** y personalidad jurídica, desde 2016 puede quedar sujeta al Impuesto sobre Sociedades ( conviene analizar el caso).

### 2.2. NIF vs “CIF”

En el lenguaje cotidiano se dice “CIF”. Oficialmente, la AEAT usa **NIF** también para entidades. Para sociedades civiles / entidades sin personalidad jurídica el NIF suele empezar por **E** (u otra letra según tipo). Hablar de “CIF definitivo” = **NIF definitivo**.

### 2.3. Obligación clave antes de cobrar

Según el procedimiento de asignación de NIF de la AEAT (procedimiento G324 / modelo 036):

> Las personas jurídicas o entidades sin personalidad jurídica que vayan a ser titulares de relaciones con trascendencia tributaria **deberán solicitar un NIF** mediante el **modelo 036**, y hacerlo **antes de** realizar entregas, prestaciones, adquisiciones, **percepción de cobros o abono de pagos**, o contratación de personal.

Esto es el punto central del documento: **cobrar por PayPal “a nombre de la SC” sin NIF choca con la lógica censal tributaria**, aunque PayPal permita teclear un registro a medias.

---

## 3. NIF provisional y NIF definitivo (AEAT)

### 3.1. NIF provisional

Se obtiene presentando el **modelo 036** de alta en el Censo de Empresarios, Profesionales y Retenedores, aportando al menos:

- Documento firmado de constitución / pacto de socios (contrato de sociedad civil, escritura o documento fehaciente equivalente).
- Datos de socios, domicilio fiscal, epígrafe IAE / actividad, obligaciones tributarias previstas.
- Identificación de representantes.

La AEAT puede asignar el NIF en unos **10 días hábiles** (plazo orientativo del procedimiento). Mientras falte documentación plena (estatutos definitivos, inscripción registral si procede, etc.), el NIF es **provisional**.

### 3.2. NIF definitivo

Cuando se aporta la documentación pendiente, se presenta de nuevo el **modelo 036 de modificación**, marcando la casilla de solicitud de **NIF definitivo** (casilla 120 en la guía del 036). Cumplida la obligación, la AEAT asigna el NIF definitivo.

### 3.3. Plazos y riesgos del provisional

- Hay obligación de aportar lo pendiente en el plazo que marca la normativa (en muchos casos, **un mes** desde el otorgamiento/inscripción que complete el expediente).
- Si no se aporta tras requerimiento, la AEAT puede **revocar el NIF provisional**.
- Un NIF revocado deja a la entidad sin identificación fiscal válida: impacto grave en facturación, bancos y PayPal.

### 3.4. Implicación para PayPal

Para PayPal, el NIF provisional **es un número de identificación fiscal real** emitido por organismo oficial. En la práctica suele bastar para:

- dar de alta la entidad en el formulario Business;
- superar verificaciones posteriores (si se aporta la carta/documento AEAT);
- vincular cuenta bancaria a nombre de la SC (cuando el banco también acepte el provisional).

Por tanto, **el NIF provisional es el verdadero “puente temporal”**, no una cuenta PayPal especial.

---

## 4. Qué exige PayPal (España / EEE)

### 4.1. Tipos de cuenta

| Tipo | Uso previsto | Idoneidad para una SC |
|---|---|---|
| **Personal** | Pagos personales, gastos compartidos, uso no comercial principal | **No apta** como cuenta operativa de la SC. Usarla para ventas/donativos de negocio vulnera condiciones y dificulta la justificación fiscal. |
| **Business** | Recibir pagos por ventas o donativos; uso comercial | **La adecuada** para la SC (o para un autónomo/socio si se opera a título personal, cosa distinta). |

Las condiciones de uso de PayPal para España indican, entre otras cosas:

- Personas físicas: mayoría de edad y capacidad.
- Personas jurídicas: la empresa debe estar en condiciones de formalizar contrato; el texto estándar habla de inscripción en registro mercantil español (las SC a menudo **no** están en ese registro, lo que puede generar fricción en verificación).
- Las cuentas Business están pensadas para personas y organizaciones **constituidas o no** que reciben pagos online por ventas o donativos.
- PayPal puede exigir **número de identificación fiscal** y documentación; si no se aporta, puede haber **limitaciones, retenciones o bloqueos**.

### 4.2. Datos habituales al crear Business

Según la propia información de alta de PayPal Business en España, suelen pedirse:

1. Nombre legal completo de la entidad (o del titular).
2. Correo y contraseña.
3. **Número de registro / identificación de la empresa** (en España: NIF).
4. Descripción de la actividad.
5. Datos de **cuenta bancaria de la empresa** (idealmente a nombre de la SC).
6. Datos del representante (DNI/NIE, domicilio, etc.).
7. En verificación posterior: documentos de identidad, domicilio, existencia de la empresa, extractos, contrato social, etc.

### 4.3. Documentación de verificación (orientativa)

PayPal verifica primero contra bases de datos. Si no localiza la entidad (muy frecuente en SC recién creadas), pedirá documentos. Orientativamente:

- **Identidad del representante:** DNI/NIE o pasaporte.
- **Domicilio:** factura de suministros, extracto bancario, etc.
- **Identidad fiscal de la empresa:** documento oficial con nombre completo + NIF (carta/certificación AEAT de asignación de NIF, modelo 036 sellado/justificante, certificado censal).
- **Existencia / constitución:** contrato de sociedad civil, escritura, estatutos, alta IAE si se aporta, etc.
- **Cuenta bancaria:** extracto a nombre de la entidad o del titular declarado.

**Nota:** algunas páginas de ayuda de PayPal mezclan terminología estadounidense (EIN/SSN). En España, el equivalente práctico es el **NIF de la entidad** y el **DNI/NIE del representante**.

### 4.4. ¿PayPal acepta NIF provisional?

PayPal no publica un producto “NIF provisional OK / KO”. En la práctica:

- El campo de alta suele aceptar el número.
- La verificación documental se supera mejor si se aporta **documento AEAT** donde conste el NIF (aunque diga provisional).
- El riesgo aparece si el provisional se **revoca** o si el nombre legal de la SC no coincide exactamente con el registrado en PayPal/banco.

**Recomendación:** usar siempre el **mismo nombre legal exacto** en contrato SC, modelo 036, banco y PayPal.

---

## 5. Escenarios posibles (de mejor a peor)

### Escenario A — Recomendado: NIF provisional → PayPal Business de la SC

1. Firmar contrato de SC.
2. Presentar modelo 036 y obtener **NIF provisional**.
3. Abrir cuenta bancaria de la SC (si el banco lo permite con provisional) o, en su defecto, preparar el circuito documental.
4. Crear **PayPal Business** a nombre de la SC con ese NIF.
5. Verificar identidad y entidad.
6. Cobrar, facturar y contabilizar a nombre de la SC.
7. Al obtener NIF definitivo: actualizar 036 (casilla 120) y datos en PayPal/banco si cambia algo (normalmente el número se mantiene y pasa a definitivo).

**Ventajas:** alineado con AEAT y con PayPal; justificación limpia; menos riesgo de mezcla de patrimonios.  
**Inconveniente:** hay que esperar días a tener el provisional antes de cobrar.

### Escenario B — Puente de emergencia: cuenta Business de un socio (autónomo) o Personal convertida, con mandato interno

Solo si **aún no hay NIF** y existe urgencia absoluta de cobrar algo puntual:

1. Un socio cobra con su PayPal (idealmente Business a su nombre si ya es autónomo).
2. Existe **acuerdo escrito** de la SC: el socio actúa como **mandatario/cobrador fiduciario** por cuenta de la sociedad en constitución/alta.
3. Cada cobro se registra en un **libro auxiliar** de la SC.
4. Se emite la documentación fiscal correcta según quién sea el obligado (ver §7).
5. En cuanto exista NIF, se abre la PayPal de la SC y se **deja de usar** la del socio.
6. Se regulariza el saldo (transferencia a la cuenta de la SC) con concepto claro.

**Riesgos:**
- Condiciones de uso de PayPal (uso comercial / titularidad real).
- Hacienda puede entender que el ingreso es del socio (y lo es formalmente si factura él).
- Conflictos entre socios si no hay acta/mandato.
- Dificultad de probar que el dinero “era de la SC” y no una donación/préstamo opaco.

### Escenario C — Evitar: cuenta Personal “de la empresa” sin alta, sin facturas, sin rastro

Cobrar donativos/ventas en una PayPal personal, sin NIF, sin facturas, sin contrato SC y “ya se verá”.  
**No es viable** como procedimiento serio: riesgo de bloqueo PayPal, sanciones tributarias, imposibilidad de justificar el origen/destino del dinero y problemas bancarios (AML).

---

## 6. Procedimiento detallado recomendado (paso a paso)

### Fase 0 — Preparación societaria

1. **Redactar y firmar el contrato de sociedad civil** (privado o ante notario según necesidad):
   - Identidad de socios y porcentajes.
   - Objeto social / actividad.
   - Domicilio.
   - Normas de administración y representación (quién puede abrir cuentas y firmar).
   - Régimen de atribución de resultados.
2. Acordar por escrito **quién será el representante** ante AEAT, banco y PayPal.
3. Reservar **nombre comercial** y correo corporativo (p. ej. `pagos@…`) para la cuenta Business.
4. Definir si la actividad será de **ventas**, **servicios** o **recaudación/donativos** (esto afecta a IVA, facturación y categoría PayPal).

### Fase 1 — Alta censal y NIF provisional

1. Cumplimentar **modelo 036**:
   - Alta en censo.
   - Solicitud de NIF (provisional si falta documentación).
   - Epígrafe IAE / actividad.
   - Obligaciones (IVA, retenciones, etc.) según el caso.
2. Aportar contrato SC + DNI/NIE de socios/representante + domicilio.
3. Presentar en AEAT (telemático según disponibilidad/certificado, o presencial según el caso).
4. Conservar:
   - Justificante de presentación.
   - Documento/carta de asignación del **NIF provisional**.
5. **No iniciar cobros** hasta tener NIF (salvo escenario B documentado).

### Fase 2 — Cuenta bancaria

1. Solicitar cuenta a nombre de la SC con NIF provisional.
2. Si el banco exige NIF definitivo:
   - Preguntar por cuenta provisional / cuenta de socios con mandato.
   - Documentar la decisión.
3. Guardar certificado de titularidad IBAN (PayPal lo pedirá a menudo).

### Fase 3 — Alta PayPal Business

1. Entrar en PayPal España → **Crear cuenta → Business**.
2. Introducir:
   - Nombre legal exacto de la SC.
   - NIF provisional.
   - Actividad y web (si existe; en proyectos de recaudación, la landing ayuda).
   - Datos del representante.
3. Vincular el IBAN.
4. Completar verificación KYC cuando PayPal la solicite (subir PDF claros, no recortados, no caducados).
5. Configurar:
   - Correo de notificaciones.
   - Usuarios/equipo (si aplica).
   - Preferencias de divisa (EUR).
   - Retiros automáticos o manuales a la cuenta bancaria de la SC.

### Fase 4 — Operativa temporal (con NIF provisional)

1. Cobrar **solo** a través de la PayPal Business de la SC.
2. Emitir factura/recibo según naturaleza del ingreso (ver §7).
3. Exportar mensualmente el CSV de actividad PayPal.
4. Conciliar PayPal ↔ banco ↔ libro de ingresos.
5. Separar comisiones PayPal como gasto.

### Fase 5 — Paso a NIF definitivo

1. Aportar a AEAT la documentación pendiente + **036 modificación (casilla 120)**.
2. Obtener confirmación de NIF definitivo.
3. Actualizar:
   - PayPal (datos fiscales / documentos).
   - Banco.
   - Facturas y pie legal de la web.
4. Archivar el historial completo del periodo provisional (es el que más suelen pedir en comprobaciones).

---

## 7. Cómo justificar la cuenta y los ingresos “temporales”

La justificación tiene **tres capas**: frente a PayPal, frente a Hacienda y frente a los socios.

### 7.1. Frente a PayPal (titularidad y uso)

Objetivo: demostrar que la cuenta es de una actividad real y lícita.

**Expediente PayPal recomendado (carpeta digital):**

1. Contrato de SC firmado.
2. Modelo 036 + NIF provisional (y luego definitivo).
3. DNI/NIE del representante y acreditación de facultades.
4. Extracto/certificado bancario.
5. Descripción de actividad + URL del proyecto.
6. Si hubo puente con cuenta de socio: **acta/mandato** + listado de transferencias de regularización.

Mantener **coherencia de nombres** en todos los documentos.

### 7.2. Frente a Hacienda (naturaleza y atribución del ingreso)

#### A) Si cobra la SC con su NIF (Escenario A)

- El ingreso es de la **entidad en atribución de rentas** (caso típico de SC sin objeto mercantil).
- Se registra en la contabilidad/libros de la SC.
- Al cierre, se **atribuye a cada socio** según pacto (o a partes iguales si no consta).
- Cada socio declara su parte en IRPF (rendimientos de actividad económica, si esa es la calificación).
- IVA: según actividad y reglas de localización; si hay IVA, modelos 303/390 u obligaciones que correspondan al alta censal.
- Conservar: facturas emitidas, CSV PayPal, extractos, contratos con clientes/donantes, cuadre de comisiones.

#### B) Si cobra un socio “por cuenta de la SC” (Escenario B)

Hay que elegir una calificación **explícita** y coherente; no improvisar después:

| Calificación | Qué implica | Cuándo encaja |
|---|---|---|
| **Ingreso del socio + posterior aportación a la SC** | El socio declara el ingreso; luego aporta el neto a la SC (aportación de socios). | Si el socio ya está de alta y puede facturar. |
| **Mandato / mediación documentada** | El socio cobra por cuenta de la SC; la SC es el verdadero perceptor económico. | Solo con mandato escrito, trazabilidad total y, preferiblemente, con NIF ya solicitado. Riesgo alto si la SC aún no existe fiscalmente. |
| **Préstamo del socio a la SC** | El socio declara, presta el dinero a la SC; la SC le debe. | Requiere contrato de préstamo, vencimiento y, en su caso, intereses. |
| **Donación entre socio y SC** | Puede tener implicaciones fiscales (ISD / otras). | Generalmente indeseable como “parche”. |

**Regla de oro:** la calificación fiscal debe decidirse **antes** del primer cobro puente, por escrito, y aplicarse de forma uniforme.

#### C) Qué NO justifica un ingreso

- Un concepto bancario genérico (“transferencia PayPal”) sin factura ni contrato.
- Capturas sueltas de móvil sin CSV completo.
- Mezclar gastos personales del socio con saldos de la SC.
- Decir “era temporal” sin fechas, importes y acuerdos.

### 7.3. Frente a los socios (gobierno interno)

Aunque Hacienda y PayPal estén cubiertos, la SC necesita:

1. **Acta o cláusula** autorizando la apertura de PayPal y el representante.
2. **Política de cobros**: qué se acepta (ventas, donativos, preventas).
3. **Informe periódico** de saldos PayPal/banco.
4. Si hubo cuenta puente: **liquidación firmada** del socio cobrador (importes brutos, comisiones, neto entregado, fecha).

### 7.4. Paquete mínimo de justificación por cada ingreso

Para cada cobro relevante, archivar:

1. Identificador de transacción PayPal.
2. Fecha, importe bruto, comisión, importe neto.
3. Identidad del pagador (cuando conste) y concepto.
4. Factura/recibo o certificado de donación (según caso).
5. Relación con el proyecto (pedido, campaña, hito).
6. Asiento contable / línea en libro de ingresos.
7. Si aplica, transferencia posterior a banco de la SC.

### 7.5. Contabilidad práctica del periodo provisional

Abrir, como mínimo:

- Libro de ingresos PayPal (o Excel/CSV controlado).
- Libro de comisiones y gastos.
- Cuenta de “cobros pendientes de regularizar” si hay puente.
- Registro de atribución provisional a socios (aunque la declaración formal sea anual/trimestral).

**Conciliación mensual sugerida:**

```
Suma bruta cobros PayPal del mes
− Comisiones PayPal
− Reembolsos/chargebacks
= Neto teórico
± Ajustes (divisas, retenciones, retenciones PayPal)
= Neto transferido a banco
= Saldo contable de la SC
```

Cualquier diferencia debe tener explicación escrita.

---

## 8. Caso específico: recaudación de fondos / proyecto (p. ej. landing de crowdfunding interno)

Si la SC usa la web para **recaudar fondos** para un proyecto:

1. Dejar claro en la web **quién es el destinatario** (nombre legal + NIF cuando exista).
2. Distinguir:
   - **Donativo** (sin contraprestación) vs
   - **Aportación con recompensa/preventa** (suele ser entrega de bien/servicio → factura e IVA si procede).
3. No presentar una PayPal personal anónima como “cuenta de la empresa”.
4. Guardar capturas de la campaña y condiciones publicadas (prueba de destino de los fondos).
5. Si los fondos son de terceros para un fin concreto, valorar si hay obligaciones adicionales (transparencia, posibles regímenes especiales). No asumir que “donativo” = exento automáticamente.

---

## 9. Checklist operativo

### Antes del primer cobro

- [ ] Contrato SC firmado
- [ ] Representante designado por escrito
- [ ] Modelo 036 presentado
- [ ] NIF provisional recibido
- [ ] Decisión documentada: Escenario A (preferido) o B (emergencia)
- [ ] Cuenta bancaria o circuito de tesorería definido
- [ ] PayPal Business creada con nombre = nombre legal
- [ ] Verificación KYC iniciada/completada
- [ ] Plantilla de factura/recibo lista
- [ ] Carpeta de expediente (AEAT + PayPal + socios)

### Durante el periodo provisional

- [ ] Export CSV mensual PayPal
- [ ] Conciliación con banco
- [ ] Facturas/recibos emitidos en plazo
- [ ] Comisiones registradas
- [ ] Sin mezclar gastos personales
- [ ] Actas de movimientos relevantes entre socios

### Al llegar el NIF definitivo

- [ ] 036 modificación (casilla 120) + docs pendientes
- [ ] Actualización PayPal/banco/web
- [ ] Cierre del periodo provisional archivado
- [ ] Si hubo puente: liquidación final firmada y saldo a cero en cuenta personal

---

## 10. Riesgos principales y cómo mitigarlos

| Riesgo | Consecuencia | Mitigación |
|---|---|---|
| Cobrar sin NIF | Incumplimiento censal; dificultad de justificar | Esperar NIF provisional; no cobrar |
| Usar PayPal personal del socio sin mandato | Atribución al socio; conflicto interno; posible limitación PayPal | Mandato escrito + liquidación + migración rápida |
| Nombre distinto en contrato / AEAT / PayPal | Fallo de verificación; bloqueos | Unificar denominación exacta |
| NIF provisional revocado | Parálisis de cobros y facturas | Cumplir plazos de documentación definitiva |
| No guardar CSV/facturas | Imposibilidad de probar ingresos/gastos | Archivo mensual + copias fuera de PayPal |
| Mezcla patrimonio socio/SC | Problemas en IRPF y entre socios | Cuentas separadas; prohibir gastos personales |
| Donativos mal calificados | IVA/IRPF incorrectos | Definir naturaleza jurídica de cada cobro |
| Retrasos de verificación PayPal | Fondos retenidos | Subir docs claros al primer aviso; responder rápido |

---

## 11. Preguntas frecuentes

**¿Puedo poner el NIF de un socio en la PayPal Business “de la empresa”?**  
No es correcto si la cuenta se presenta como de la SC. El NIF debe ser el de la entidad titular. Si la cuenta es del socio, entonces la titularidad (y normalmente la tributación inicial) es del socio.

**¿El NIF provisional caduca solo?**  
No “caduca” como un carné con fecha, pero **sí puede revocarse** si no se completa el expediente tras requerimiento.

**¿Hacienda ve los movimientos de PayPal?**  
Los prestadores de servicios de pago tienen obligaciones de información en el marco europeo (p. ej. reporting de pagos). Además, en comprobaciones se pueden requerir extractos. Conviene trabajar **como si todo fuera visible**.

**¿Puedo abrir PayPal Business el mismo día del 036?**  
Puedes intentarlo, pero sin NIF aún no tendrás el dato fiscal correcto. Lo sensato es esperar la asignación del NIF provisional.

**¿Una SC no inscrita en el Registro Mercantil puede tener PayPal Business?**  
Las condiciones hablan de organizaciones constituidas o no, y de personas jurídicas inscritas. En SC es frecuente la fricción documental. Mitigación: contrato sólido, NIF AEAT, extractos y coherencia total de datos. Si PayPal rechaza el tipo societario, alternativas: operar vía socio autónomo (con marco interno) o valorar otra forma jurídica.

**¿Qué hago con los ingresos ya cobrados en una cuenta personal “temporal”?**  
1) Parar cobros nuevos en esa cuenta.  
2) Inventariar transacciones.  
3) Firmar acuerdo de regularización entre socios.  
4) Transferir el neto a la cuenta de la SC cuando exista.  
5) Declarar según la calificación elegida (asesor).  
6) Abrir/usar ya la PayPal Business de la SC.

---

## 12. Modelo breve de mandato interno (puente de emergencia)

> **Acuerdo de cobro temporal por cuenta de la Sociedad Civil**  
> Los socios de la SC “[NOMBRE]”, en constitución/alta censal, autorizan a [NOMBRE DEL SOCIO], DNI/NIE […], a recibir cobros a través de su cuenta PayPal [email/ID] **exclusivamente** por cuenta y en interés de la SC, desde [fecha] hasta la fecha en que la SC disponga de NIF y cuenta PayPal Business propia.  
> El socio cobrador se obliga a: (i) no disponer de los fondos para uso personal; (ii) llevar relación diaria de cobros/comisiones; (iii) transferir el neto a la cuenta de la SC en el plazo máximo de [X] días desde que exista IBAN de la SC; (iv) entregar CSV y justificantes.  
> La calificación fiscal de estos cobros será la que determine el asesor de la SC, de forma coherente con el alta censal y las facturas emitidas.  
> Firmas de todos los socios · Fecha · Lugar

Este modelo es orientativo; debe adaptarlo un profesional al caso.

---

## 13. Conclusión práctica

1. **No existe** una “cuenta PayPal temporal oficial” sustitutiva del NIF/CIF.
2. El instrumento temporal correcto en España es el **NIF provisional** de la AEAT (modelo 036).
3. Con ese NIF, la vía limpia es una **PayPal Business a nombre de la SC**.
4. Cobrar antes del NIF solo debería plantearse como **excepción documentada**, con mandato, trazabilidad y regularización inmediata.
5. Justificar ingresos temporales = **titularidad clara + facturas/recibos + CSV + conciliación + acuerdo entre socios + declaración coherente en atribución de rentas / IRPF (o IS, si aplica)**.

---

## 14. Referencias útiles (consulta)

- AEAT — Asignación de NIF a personas jurídicas y entidades sin personalidad jurídica (procedimiento G324): modelo 036, NIF provisional/definitivo.  
- AEAT — Guía del modelo 036, casilla 120 (NIF definitivo).  
- AEAT — Régimen de atribución de rentas (sociedades civiles sin objeto mercantil / sin personalidad).  
- PayPal España — Alta cuenta Business; Condiciones de uso; ayuda de documentos para confirmar entidad comercial.  

---

## 15. Anexo: mapa de decisión

```
¿Existe contrato de SC firmado?
 ├─ No → Firmarlo antes de cualquier cobro
 └─ Sí
     ¿Hay NIF (provisional o definitivo)?
      ├─ No → Presentar 036; NO cobrar (o solo Escenario B documentado)
      └─ Sí
          ¿PayPal Business a nombre de la SC verificada?
           ├─ No → Crearla con NIF + docs AEAT/banco
           └─ Sí → Cobrar, facturar, conciliar, archivar
                    ¿NIF aún provisional?
                     ├─ Sí → Completar docs y pedir definitivo (036 casilla 120)
                     └─ No → Mantener expediente y obligaciones periódicas
```

---

## 16. Problemas legales y financieros que puede ocasionar

Operar con PayPal “de forma temporal” sin NIF definitivo —o, peor, sin NIF provisional y sin documentación— no es un detalle administrativo menor. Puede generar **daños legales, fiscales, contractuales y de tesorería** que afecten a la sociedad civil y, por la naturaleza de la SC, también al **patrimonio personal de los socios**.

### 16.1. Problemas legales y regulatorios

#### a) Incumplimiento del alta censal antes de cobrar

Si la SC percibe cobros, contrata o factura **sin haber solicitado NIF** (modelo 036), se incumple la lógica del censo de obligados tributarios. Eso puede derivar en:

- requerimientos de la AEAT;
- regularizaciones de oficio;
- sanciones por incumplimiento de obligaciones formales;
- dificultad para demostrar buena fe si más adelante hay inspección.

#### b) Uso indebido de la cuenta PayPal (condiciones de uso)

Cobrar actividad empresarial/donativos de proyecto en una **cuenta Personal**, u ocultar la titularidad real de los fondos, puede vulnerar las condiciones de PayPal. Consecuencias posibles:

- limitación o suspensión de la cuenta;
- retención prolongada de saldos;
- solicitud reforzada de KYC/AML;
- cierre de la cuenta y deterioro de la relación con el proveedor de pagos;
- en casos graves, comunicación a sistemas de prevención de fraude / listas internas del sector (impacto reputacional operativo).

#### c) Responsabilidad de los socios en una Sociedad Civil

En muchas SC, los socios responden de las deudas sociales de forma **personal y, según el pacto y el tipo de deuda, solidaria o mancomunada**. Un problema de la “cuenta temporal” no se queda necesariamente en la entidad: puede llegar al patrimonio del socio que cobró o de todos los socios.

#### d) Falsa representación frente a clientes, donantes o proveedores

Si la web o las comunicaciones presentan una “empresa” con PayPal personal de un particular, puede haber:

- reclamaciones por publicidad engañosa o falta de transparencia;
- derecho de desistimiento / reembolso mal gestionado;
- conflictos de consumo (si hay venta a particulares);
- pérdida de confianza y daño reputacional del proyecto.

#### e) Blanqueo de capitales y origen de fondos (AML)

Bancos y PayPal están obligados a vigilar operaciones sospechosas. Movimientos típicos de riesgo:

- cobros a nombre de una persona y transferencias inmediatas a otra;
- conceptos genéricos (“varios”, “proyecto”, “donación”) sin soporte;
- volumen creciente sin alta fiscal coherente;
- mezcla de gastos personales y saldos del proyecto.

Resultado posible: bloqueo cautelar, petición de documentación exhaustiva o cancelación de productos financieros.

#### f) Protección de datos y confidencialidad

Usar la bandeja/PayPal personal de un socio para cobros de la SC puede mezclar datos de clientes/donantes con la esfera privada del socio (RGPD): accesos indebidos, conservación irregular, dificultad para atender derechos de los interesados.

### 16.2. Problemas fiscales

#### a) Atribución incorrecta de rentas

Si cobra el socio pero el dinero “era de la SC” (o al revés), Hacienda puede:

- imputar el ingreso al socio que figura en PayPal;
- rechazar gastos o atribuciones posteriores mal documentadas;
- exigir declaraciones complementarias (IRPF, IVA, retenciones).

#### b) IVA no repercutido o repercutido mal

Preventas, recompensas o servicios cobrados como “donativo” pueden ser entregas sujetas a IVA. No emitir factura / no declarar el 303 puede generar:

- cuota de IVA + intereses de demora;
- recargos por declaración extemporánea;
- sanciones.

#### c) Sanciones por obligaciones formales

Además de la cuota, hay riesgo de sanción por:

- no presentar o presentar tarde el 036;
- no llevar libros/registros exigibles;
- no emitir factura cuando procede;
- no conservar justificantes el plazo legal.

#### d) Revocación del NIF provisional

Si se obtuvo NIF provisional pero no se completa el expediente, la AEAT puede revocarlo. Efectos:

- imposibilidad de facturar válidamente;
- fricción o corte con banco y PayPal;
- necesidad de regularizar cobros ya realizados bajo un NIF luego anulado.

#### e) Doble imposición práctica o “pagar dos veces” el mismo hecho

Un mal puente (socio declara + SC también atribuye sin cuadrar) puede provocar que el mismo ingreso se declare mal dos veces, o que un socio pague de más y otro de menos, generando después conflictos de compensación entre socios.

### 16.3. Problemas financieros y de tesorería

#### a) Fondos retenidos o inaccesibles

PayPal puede retener saldos por verificación, reclamaciones (chargebacks) o revisión de riesgo. Si la única caja del proyecto está ahí:

- no se pueden pagar proveedores;
- se retrasan hitos del proyecto;
- aumenta la presión para “sacar el dinero” por vías peores (más riesgo).

#### b) Chargebacks y reversiones

El titular formal de la cuenta (a menudo el socio) asume la gestión y, en la práctica, el golpe de tesorería de devoluciones. Si el saldo ya se gastó en el proyecto, el socio puede quedar **descubierto personalmente**.

#### c) Comisiones, tipos de cambio y fugas de margen

Sin control CSV/conciliación, las comisiones PayPal, conversiones de divisa y microcargos erosionan el presupuesto sin que la SC lo mida. En recaudaciones pequeñas, esa fuga puede ser material.

#### d) Mezcla de patrimonios (commingling)

Introducir fondos del proyecto en la cuenta personal del socio:

- dificulta saber qué dinero es de la SC;
- complica embargos, herencias, divorcios o deudas personales del socio;
- puede hacer que acreedores del socio pretendan cobrar sobre saldos que “eran del proyecto”;
- o que acreedores del proyecto pretendan cobrar al socio sin rastro claro de mandato.

#### e) Imposibilidad de abrir banca / obtener financiación

Historial de irregularidades, cuentas limitadas o falta de estados claros dificulta:

- apertura de cuenta bancaria a nombre de la SC;
- pasarelas de pago alternativas;
- ayudas, subvenciones o acuerdos con partners que exigen NIF y trazabilidad.

#### f) Parálisis del proyecto por dependencia de una sola persona

Si solo un socio controla la PayPal “temporal”:

- enfermedad, disputa o salida de ese socio puede dejar los fondos fuera de alcance;
- el resto de socios puede no tener legitimación práctica ante PayPal para recuperar el saldo.

### 16.4. Problemas entre socios y frente a terceros

#### a) Conflictos societarios internos

Sin mandato ni liquidación firmada, es frecuente discutir:

- quién se queda con el saldo;
- quién asume comisiones e impuestos;
- si un cobro fue aportación, préstamo o ingreso de la SC;
- si el socio cobrador debe intereses o indemnización por retrasos.

Estos conflictos pueden acabar en reclamación civil entre socios.

#### b) Responsabilidad frente a donantes/clientes

Si se prometió un destino concreto de los fondos y la tesorería se diluye en cuentas personales, terceros pueden exigir:

- reembolso;
- cumplimiento de la contraprestación;
- información sobre el uso del dinero.

#### c) Pérdida de oportunidades comerciales

Empresas, sponsors o plataformas suelen exigir factura con NIF. Operar “en provisional caótico” puede hacer perder contratos precisamente cuando el proyecto empieza a generar tracción.

### 16.5. Escenarios de daño acumulado

| Situación | Efecto legal | Efecto financiero |
|---|---|---|
| Cobros meses sin 036 ni facturas | Requerimiento AEAT + posibles sanciones | Regularización con intereses; caja improvisada |
| PayPal personal del socio sin mandato | Condiciones PayPal + conflicto societario | Saldo retenido o disputa por titularidad |
| NIF provisional revocado a mitad de campaña | Facturas cuestionadas; corte de proveedores | Campaña frenada; reembolsos masivos |
| Donativos mal calificados como venta (o al revés) | IVA/IRPF incorrectos | Cuotas + recargos inesperados |
| Embargo de la cuenta personal del socio cobrador | Terceros ajenos al proyecto entran en la caja | Fondos del proyecto afectados por deudas privadas |
| Cierre PayPal por KYC fallido | Pérdida del canal de cobro | Importe atrapado + coste de migrar a otra pasarela |

### 16.6. Señales de alarma (parar y regularizar)

Conviene **detener cobros nuevos** y pedir asesoramiento si aparece cualquiera de estas señales:

1. PayPal pide documentación y no se puede aportar NIF ni contrato SC.
2. El banco pregunta el origen de transferencias reiteradas desde PayPal personal.
3. Un socio ha usado fondos del proyecto para gastos personales “a devolver”.
4. Hay donantes/clientes pidiendo factura y no existe NIF.
5. Los socios no coinciden en cuánto hay en caja ni a quién pertenece.
6. Llega un requerimiento de AEAT, PayPal o el banco.
7. El NIF provisional está pendiente de documentación fuera de plazo.

### 16.7. Coste de prevenir frente a coste de remediar

| Enfoque | Coste típico | Resultado |
|---|---|---|
| **Prevenir:** 036 + NIF provisional + PayPal Business + mandato interno | Tiempo administrativo + posible asesoría inicial | Trazabilidad, menos bloqueos, socios protegidos |
| **Remediar:** inspecciones, bloqueos, sanciones, abogados, reembolsos | Muy superior; además daño reputacional y paro del proyecto | Recuperación incierta; a veces irreversible |

**Conclusión de este apartado:** los problemas no son solo “que Hacienda se enfade”. Una cuenta PayPal temporal mal planteada puede **bloquear la caja, personalizar deudas, romper la confianza entre socios y comprometer la continuidad del proyecto**. Por eso el documento insiste en el NIF provisional como puente legítimo y en documentar cualquier excepción como lo que es: una emergencia breve, no un método de trabajo.

---

*Documento preparado para el repositorio del proyecto (Proyecto Icarus). Revisar periódicamente frente a cambios de PayPal y de la AEAT.*  
*[Volver al índice](#índice)*
