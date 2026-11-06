# June Skills — Maestro de Growth e Performance

Skills de IA (Claude) da **June** para atender clientes de **negócio local, ecommerce e híbridos**: diagnóstico de todos os canais, plano de ação, CRO, CRM, SEO, GEO, Google Meu Negócio, mídia paga (Meta e Google Ads), calendário comercial, campanhas de site, dados e relatórios diários/semanais/mensais, social media, design e vídeo.

O centro de tudo é o **`june-maestro`**: a porta de entrada que entende o pedido, carrega o contexto do cliente, escolhe as skills certas, define a ordem e cobra o padrão June.

```
                          ┌──────────────────────┐
     pedido / cliente ──▶ │     june-maestro     │ ◀── rotina: diário · sexta · mês · trimestre
                          └──────────┬───────────┘
        ┌──────────────┬─────────────┼──────────────┬───────────────┬──────────────┐
   Diagnóstico      Dados (sexta 14h)   Estratégia (mês)   Campanhas        Produção
   june-diagnostico june-*-dados        june-*-estrategia  june-calendario  june-designer-artes
   -plano-acao      june-gmn-local      june-geo-ia        -comercial       june-roteiro-video
                    june-ecommerce-     june-midia-        june-campanhas-  june-reels-modelagem
                    dados               estrategia         site             june-*-socialmidia
                          └────────▶ june-growth-cerebro (sexta 16h) ──▶ june-relatorios (diário/mensal)
                                     ▲
             skills de mercado (mkt-*) = consultores de apoio para aprofundar cada tema
```

## O que tem aqui

| Plugin | Skills | O que cobre |
|---|---|---|
| **`june-agencia`** | 23 | Maestro + skills June (donas da entrega, em PT-BR, no padrão da agência) |
| `mkt-growth-cro-crm` | 34 | CRO, A/B, pop-ups, analytics, rastreio, atribuição, e-mail, SMS, ads, criativos, copy, oferta, SEO, AI SEO, conteúdo, pesquisa de cliente, concorrência, influência, eventos, lançamentos |
| `mkt-local-gmn` | 20 | Google Meu Negócio, posts, avaliações, citações, geogrid, páginas locais, multi-unidades, área de atendimento, suspensão, Google Maps |
| `mkt-geo-ia` | 9 | GEO: auditoria de visibilidade em IA, citabilidade, llms.txt, robôs de IA, schema, menções de marca |
| `mkt-midia-ecommerce` | 14 | Shopify, Google Ads, Meta Ads, TikTok Ads, GA4, GTM, Looker Studio, Klaviyo, CRO, verba desperdiçada, UTM/atribuição, Biblioteca de Anúncios, auditoria multiplataforma |

Lista completa com descrição: **[CATALOGO.md](CATALOGO.md)**.

### Skills June
**Novas neste repositório:** `june-maestro`, `june-gmn-local`, `june-geo-ia`, `june-calendario-comercial`, `june-campanhas-site`, `june-ecommerce-dados`, `june-midia-estrategia`, `june-relatorios`.

**Já existentes (consolidadas aqui):** `june-diagnostico-plano-acao`, `june-growth-cerebro`, `june-cro-dados`, `june-cro-estrategia`, `june-crm-dados`, `june-crm-estrategia`, `june-seo-dados`, `june-seo-estrategia`, `june-midia-dados`, `june-linha-editorial-socialmidia`, `june-calendario-conteudo-socialmidia`, `june-analise-resultados-socialmidia`, `june-designer-artes`, `june-roteiro-video`, `june-reels-modelagem`.

## Como instalar

### Claude Code (recomendado: tudo de uma vez, com atualização)
```bash
claude plugin marketplace add bi208/claude-skills
```
```bash
claude plugin install june-agencia@june-skills
```
Depois instale os plugins de apoio que quiser:
```bash
claude plugin install mkt-growth-cro-crm@june-skills
```
```bash
claude plugin install mkt-local-gmn@june-skills
```
```bash
claude plugin install mkt-geo-ia@june-skills
```
```bash
claude plugin install mkt-midia-ecommerce@june-skills
```
(No app, o mesmo pode ser feito pelo comando `/plugin`.) Nos plugins, as skills aparecem com prefixo, ex.: `june-agencia:june-maestro`.

### Claude.ai / Claude Desktop (skills da organização ou pessoais)
Gere um `.zip` por skill e faça upload em *Configurações → Capacidades → Skills* (ou no painel de skills da organização):
```bash
bash scripts/empacotar_zips.sh
```
Os arquivos saem em `dist/<plugin>/<skill>.zip`. Para subir só as skills June: `bash scripts/empacotar_zips.sh june-agencia`.

### Opcionais externos (com scripts e agentes próprios)
Duas suítes muito boas dependem de scripts Python e agentes, então não foram copiadas — instale direto da fonte se quiser:
- **claude-seo** (AgriciDaniel) — auditoria técnica de SEO, schema, ecommerce, DataForSEO: `claude plugin marketplace add AgriciDaniel/claude-seo`
- **claude-ads** (AgriciDaniel) — auditoria e criação de anúncios multiplataforma: `claude plugin marketplace add AgriciDaniel/claude-ads`

## Como usar no dia a dia
- *"Chegou o cliente X (ecommerce na Nuvemshop). Monta o diagnóstico e o plano."* → maestro → Fluxo A
- *"Roda a rotina de sexta do cliente Y."* → relatórios de canal → cérebro
- *"Pulso de hoje do cliente Z."* → `june-relatorios` (diário)
- *"Planeja o Dia das Mães da loja W: site, CRM, Meta e Google."* → calendário comercial → campanhas de site → canais → produção
- *"As vendas caíram 30% essa semana, por quê?"* → maestro → Fluxo D
- *"Como a clínica aparece no ChatGPT e no Google Maps?"* → `june-geo-ia` + `june-gmn-local`

## Padrões da June
- **Relatório Padrão de Canal June v1** — definido em `june-growth-cerebro` (seção 3). Canais: `ads`, `crm`, `seo`, `cro`, `social`, `ecommerce` e `local` (novo, entregue por `june-gmn-local`).
- **Cadência:** pulso diário até 10h · relatórios de canal sexta 14h · cérebro sexta 16h · fechamento mensal dias 1–3 · planos do mês até dia 20 · calendário comercial trimestral.
- **Fonte de verdade:** plataforma da loja > GA4 > gerenciadores de Ads > CRM. Nunca somar receitas atribuídas.
- **Só leitura até aprovar** qualquer mudança em conta de cliente.

## Manutenção
- Editou uma skill? Rode `python3 scripts/gerar_catalogo.py` para atualizar o catálogo e o mapa do maestro.
- Valide os manifestos: `claude plugin validate .`
- Atualizar skills de mercado: copie de novo da fonte (ver [CREDITS.md](CREDITS.md)) e revise as diferenças.

## Créditos e licenças
As skills `mkt-*` são de terceiros, sob licença MIT, copiadas sem alteração de conteúdo (exceto ajustes de caminho de referências). Ver [CREDITS.md](CREDITS.md). As skills `june-*` são de uso interno da June.
