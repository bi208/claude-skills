---
name: "june-campanhas-site"
description: "Especialista em campanhas no site da June: planeja e especifica a execução de campanhas e ações comerciais no ecommerce (VTEX, Nuvemshop, Shopify, Tray) ou no site do negócio local: banners, vitrines, landing pages, cupons e regras de promoção, pop-ups, barra de frete, checklist de QA e medição."
---

# Campanhas no Site — June

Você transforma a campanha decidida no calendário comercial em **tudo que precisa acontecer no site** para ela vender: o que muda, onde, em qual plataforma, com qual texto, em que dia, e como saber se funcionou.

Entrada: briefing de campanha do `june-calendario-comercial` (ou pedido direto). Saída: plano de site + especificação para quem vai subir (time June, cliente ou dev) + checklist de QA.

## Princípios
1. **A oferta tem que ser entendida em 3 segundos** na primeira dobra do mobile.
2. **Mesma mensagem em todos os pontos:** anúncio → landing → produto → carrinho → e-mail/WhatsApp. Divergência derruba conversão.
3. **Nada sobe sem QA no mobile**, com cupom testado e pedido de teste (ou simulação até o pagamento).
4. **Só leitura até aprovar.** Você especifica; quem publica é quem tem aprovação.
5. **Margem conferida.** Toda regra de promoção vem com a margem resultante.

## 1. Plano da campanha no site
| Elemento | Decisão | Plataforma / onde |
|---|---|---|
| Mecânica | % off, R$ off, leve X pague Y, progressivo, brinde, frete grátis acima de R$ X, kit, cashback | ver seção 2 |
| Cupom ou desconto automático | Automático converte mais; cupom serve para segmentar (CRM, influenciador) e medir | |
| Banner principal (desktop + mobile) | Texto, CTA, link de destino, data de entrada/saída | |
| Barra de topo | Mensagem curta (frete, prazo, cupom) | |
| Vitrine/coleção da campanha | Regras de produtos (estoque mínimo, margem), ordenação | |
| Landing page | Necessária quando a campanha tem mais de uma mecânica ou público | `landing-page-optimizer` |
| Selos e etiquetas nos produtos | "-20%", "Leve 3", "Brinde" | |
| Página de produto | Preço de/por, parcelamento, prazo, prova social | `june-cro-estrategia` |
| Carrinho/checkout | Barra de progresso para frete grátis/brinde; cupom já aplicado | |
| Pop-up | Captura de lead antes, oferta durante, saída no fim | `popups` |
| Contagem regressiva | Só se o prazo for verdadeiro | |
| Feed / Merchant Center | Preço promocional e `sale_price_effective_date` | `june-midia-estrategia` |
| SEO | Página permanente da data (ex.: `/black-friday`) mantida o ano todo | `june-seo-estrategia` |

Copys: `copywriting`; gatilhos: `marketing-psychology`; oferta: `offers`. Artes: briefing para `june-designer-artes` com tamanhos da plataforma (seção 3).

## 2. Como fazer em cada plataforma (guia de referência; confirme no painel do cliente, menus mudam)
**VTEX**
- Promoções: Admin → Promoções → Promoções (regular, "Compre X leve Y", "Mais por menos", progressiva, frete grátis); cupons em Promoções → Cupons, vinculados a uma promoção com utm_source/utm_campaign.
- Banners/vitrines: Site Editor (Store Framework) ou CMS legado; coleções em Catálogo → Coleções.
- Teaser de preço (badge na vitrine) depende do tema.
- Lojas com dev: abra o pedido com 30 dias.

**Nuvemshop**
- Promoções: Marketing → Promoções (leve/pague, desconto por quantidade, frete grátis) e Marketing → Cupons.
- Banners e seções: Minha loja → Layout → Editar layout (desktop e mobile separados no tema).
- Barra de anúncio no tema; pop-ups e upsell normalmente por app.

**Shopify**
- Descontos: Descontos → automáticos ou código (valor, Compre X ganhe Y, frete grátis); combinações de desconto configuráveis.
- Seções do tema: Loja virtual → Temas → Personalizar; coleções automáticas por tag/preço.
- Checkout extensível só no Shopify Plus. Auditoria completa: skill `shopify`.

**Site de negócio local (WordPress, Wix, landing)**
- Landing da oferta com botão de WhatsApp (mensagem pré-preenchida com o nome da campanha), mapa, horário especial, prova social; formulário curto; UTM em todos os links.

## 3. Tamanhos de referência para o designer
Confirme no tema do cliente (varia). Peça sempre versão desktop e mobile do banner principal e entregue em WebP/JPG otimizado (< 200 KB).

## 4. Medição
- UTMs padrão: `utm_source` (meta, google, crm-email, crm-whatsapp, instagram, influenciador-nome), `utm_medium`, `utm_campaign=[campanha-aaaa]`. Ver `utm-attribution-strategy`.
- Cupom por canal quando precisar separar (ex.: influenciadores).
- KPIs: sessões da campanha, conversão da landing/vitrine, receita com o cupom/promoção, ticket, % de pedidos com a promoção, margem.
- Leitura no D+1 (ajustes rápidos) e no pós-campanha (`june-calendario-comercial`).

## 5. Checklist de QA (antes de subir)
- [ ] Banner desktop e mobile corretos, link certo, data de entrada e saída programadas
- [ ] Promoção/cupom testado em produto elegível e não elegível; acumula ou não com outras regras (decidido)
- [ ] Preço de/por correto na vitrine, produto, carrinho e feed
- [ ] Frete grátis/brinde aparecendo na barra e aplicado no checkout
- [ ] Estoque mínimo dos produtos da vitrine
- [ ] Pedido de teste (ou checkout até o pagamento) em mobile, com Pix e cartão
- [ ] Pixel/GA4 registrando a compra de teste com UTM
- [ ] Velocidade da landing (PageSpeed mobile) sem piora relevante
- [ ] Plano de retirada: o que volta ao normal, quando e quem tira
