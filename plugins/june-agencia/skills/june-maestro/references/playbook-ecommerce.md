# Playbook — Ecommerce (VTEX, Nuvemshop, Shopify, Tray e outros)

## Equação
Receita = Sessões × Taxa de conversão × Ticket médio  (+ recompra da base)
Cada alavanca tem dono:
- Sessões → Mídia (`june-midia-*`), SEO (`june-seo-*`), GEO (`june-geo-ia`), Social, CRM (tráfego da base)
- Conversão → CRO (`june-cro-*`), campanhas de site (`june-campanhas-site`), oferta
- Ticket → kits, frete grátis progressivo, cross-sell, preço (`pricing`, `offers`)
- Recompra → CRM (`june-crm-*`)

## Métricas do cérebro
MER, CAC de novos, margem de contribuição, inflação de atribuição (ver `june-growth-cerebro`). ROAS de breakeven = 1 ÷ margem bruta.

## Fundação obrigatória (antes de escalar verba)
- GA4 com eventos de ecommerce completos (view_item, add_to_cart, begin_checkout, add_payment_info, purchase) e valores certos.
- Pixel + API de Conversões da Meta com deduplicação; conversões do Google Ads (ideal: conversões otimizadas) e feed no Merchant Center sem reprovações.
- UTMs padronizadas em CRM, social e influenciadores.
- Fluxos de CRM ativos: boas-vindas, carrinho abandonado, navegação abandonada, pós-compra, reativação.
- Checkout testado em mobile, com Pix, cartão e frete calculado na página de produto.

## Particularidades por plataforma
| Plataforma | Onde olhar dados | Atenções |
|---|---|---|
| **VTEX** | Admin → Pedidos/Relatórios, Intelligent Search, Master Data | Catálogo grande: SEO de categorias/facetas, promoções e "Teaser" de preço, multi-loja/seller. Mudanças de layout via Site Editor/CMS — envolve dev. |
| **Nuvemshop** | Admin → Estatísticas, Pedidos, Nuvem Envio | Limitações de checkout; apps para avaliações, upsell e pop-up; layout por tema. Promoções nativas (progressivo, frete). |
| **Shopify** | Analytics, Relatórios, Shopify Flow, Markets | Apps (Klaviyo, Judge.me…), checkout extensível só no Plus; use a skill `shopify` para auditoria de 12 passos. |
| **Tray / Loja Integrada / WooCommerce** | Painel de relatórios | Verificar integração GA4 e pixel (frequentemente quebrada). |

## Ritmo
Ver `cadencia.md`. Datas comerciais: `june-calendario-comercial` (Black Friday é planejada a partir de agosto).

## Armadilhas comuns
- Escalar mídia com rastreio quebrado.
- Comemorar ROAS de plataforma com MER caindo.
- Desconto como única alavanca (corrói margem e treina o cliente a esperar promoção).
- Ruptura de best-seller com campanha rodando.
- Frete caro escondido até o checkout.
