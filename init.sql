CREATE TABLE IF NOT EXISTS public.sku
(
    uuid                   UUID PRIMARY KEY,
    marketplace_id         BIGINT NOT NULL,
    product_id             BIGINT NOT NULL,
    title                  TEXT,
    description            TEXT,
    brand                  TEXT,
    seller_id              INTEGER,
    seller_name            TEXT,
    first_image_url        TEXT,
    category_id            INTEGER,
    category_lvl_1         TEXT,
    category_lvl_2         TEXT,
    category_lvl_3         TEXT,
    category_remaining     TEXT,
    features               JSON,
    rating_count           INTEGER,
    rating_value           DOUBLE PRECISION,
    price_before_discounts REAL,
    discount               DOUBLE PRECISION,
    price_after_discounts  REAL,
    bonuses                INTEGER,
    sales                  INTEGER,
    inserted_at            TIMESTAMP DEFAULT NOW(),
    updated_at             TIMESTAMP DEFAULT NOW(),
    currency               TEXT,
    barcode                BIGINT,
    similar_sku            UUID[]
);

COMMENT ON COLUMN public.sku.uuid IS 'id товара в нашей бд';
COMMENT ON COLUMN public.sku.marketplace_id IS 'id маркетплейса';
COMMENT ON COLUMN public.sku.product_id IS 'id товара в маркетплейсе';
COMMENT ON COLUMN public.sku.title IS 'название товара';
COMMENT ON COLUMN public.sku.description IS 'описание товара';
COMMENT ON COLUMN public.sku.category_lvl_1 IS 'Первая часть категории товара. Например, для товара, находящегося по пути Детям/Электроника/Детская электроника/Игровая консоль/Игровые консоли и игры/Игровые консоли, в это поле запишется "Детям".';
COMMENT ON COLUMN public.sku.category_lvl_2 IS 'Вторая часть категории товара. Например, для товара, находящегося по пути Детям/Электроника/Детская электроника/Игровая консоль/Игровые консоли и игры/Игровые консоли, в это поле запишется "Электроника".';
COMMENT ON COLUMN public.sku.category_lvl_3 IS 'Третья часть категории товара. Например, для товара, находящегося по пути Детям/Электроника/Детская электроника/Игровая консоль/Игровые консоли и игры/Игровые консоли, в это поле запишется "Детская электроника".';
COMMENT ON COLUMN public.sku.category_remaining IS 'Остаток категории товара. Например, для товара, находящегося по пути Детям/Электроника/Детская электроника/Игровая консоль/Игровые консоли и игры/Игровые консоли, в это поле запишется "Игровая консоль/Игровые консоли и игры/Игровые консоли".';
COMMENT ON COLUMN public.sku.features IS 'Характеристики товара';
COMMENT ON COLUMN public.sku.rating_count IS 'Кол-во отзывов о товаре';
COMMENT ON COLUMN public.sku.rating_value IS 'Рейтинг товара (0-5)';
COMMENT ON COLUMN public.sku.barcode IS 'Штрихкод';

CREATE INDEX sku_brand_index
    ON public.sku (brand);

CREATE UNIQUE INDEX sku_marketplace_id_sku_id_uindex
    ON public.sku (marketplace_id, product_id);

CREATE UNIQUE INDEX sku_uuid_uindex
    ON public.sku (uuid);
