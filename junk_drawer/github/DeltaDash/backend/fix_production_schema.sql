-- Run this SQL directly on your production database to fix the immediate schema issues

-- Add missing columns to ammunition table
ALTER TABLE ammunition ADD COLUMN IF NOT EXISTS name VARCHAR NOT NULL DEFAULT '';
ALTER TABLE ammunition ADD COLUMN IF NOT EXISTS caliber_unit VARCHAR;
ALTER TABLE ammunition ADD COLUMN IF NOT EXISTS caliber_diameter_mm NUMERIC(10,3);
ALTER TABLE ammunition ADD COLUMN IF NOT EXISTS caliber_length_mm NUMERIC(10,3);
ALTER TABLE ammunition ADD COLUMN IF NOT EXISTS caliber_inch NUMERIC(10,4);
ALTER TABLE ammunition ADD COLUMN IF NOT EXISTS projectile_type VARCHAR;
ALTER TABLE ammunition ADD COLUMN IF NOT EXISTS nominal_velocity_fps NUMERIC(10,2);
ALTER TABLE ammunition ADD COLUMN IF NOT EXISTS nominal_velocity_m_s NUMERIC(10,2);
ALTER TABLE ammunition ADD COLUMN IF NOT EXISTS manufacturer VARCHAR;
ALTER TABLE ammunition ADD COLUMN IF NOT EXISTS lot_number VARCHAR;
ALTER TABLE ammunition ADD COLUMN IF NOT EXISTS standard_reference VARCHAR;
ALTER TABLE ammunition ADD COLUMN IF NOT EXISTS notes VARCHAR;
ALTER TABLE ammunition ADD COLUMN IF NOT EXISTS created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW();
ALTER TABLE ammunition ADD COLUMN IF NOT EXISTS updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW();

-- Create indexes on ammunition
CREATE INDEX IF NOT EXISTS ix_ammunition_caliber ON ammunition(caliber);
CREATE INDEX IF NOT EXISTS ix_ammunition_name ON ammunition(name);

-- Drop old vest table and create new vests table
DROP TABLE IF EXISTS vest;

CREATE TABLE vests (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    vest_code VARCHAR NOT NULL,
    vest_type VARCHAR,
    threat_level VARCHAR,
    protection_class VARCHAR,
    total_layers INTEGER,
    total_thickness_mm NUMERIC(10,3),
    sizes JSON,
    construction_notes VARCHAR,
    stitch_pattern VARCHAR,
    backing_material VARCHAR,
    notes VARCHAR,
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW()
);

CREATE INDEX ix_vests_vest_code ON vests(vest_code);

-- Fix alembic version table to match local migration
UPDATE alembic_version SET version_num = 'fix_ammo_vest' WHERE version_num = '8ec6d557e142';
-- If the above doesn't work, try inserting:
INSERT INTO alembic_version (version_num) VALUES ('fix_ammo_vest') ON CONFLICT (version_num) DO UPDATE SET version_num = 'fix_ammo_vest';
