namespace StarfinderSRD.Migrations
{
    using System;
    using System.Data.Entity.Migrations;
    
    public partial class initial : DbMigration
    {
        public override void Up()
        {
            CreateTable(
                "dbo.Characters",
                c => new
                    {
                        CharacterID = c.Int(nullable: false, identity: true),
                        Name = c.String(nullable: false, maxLength: 40),
                        Race = c.String(nullable: false, maxLength: 20),
                        Class = c.String(nullable: false, maxLength: 20),
                        Theme = c.String(nullable: false, maxLength: 20),
                    })
                .PrimaryKey(t => t.CharacterID);
            
            CreateTable(
                "dbo.Classes",
                c => new
                    {
                        ClassID = c.Int(nullable: false, identity: true),
                        Name = c.String(),
                        HPSP = c.Int(nullable: false),
                        Ability = c.String(),
                        SkillPoints = c.Int(nullable: false),
                        Feature = c.String(),
                    })
                .PrimaryKey(t => t.ClassID);
            
            CreateTable(
                "dbo.Races",
                c => new
                    {
                        RaceID = c.Int(nullable: false, identity: true),
                        Name = c.String(),
                        HP = c.Int(nullable: false),
                        Mod1 = c.Int(nullable: false),
                        ModAmount1 = c.Int(nullable: false),
                        Mod2 = c.Int(nullable: false),
                        ModAmount2 = c.Int(nullable: false),
                        Mod3 = c.Int(nullable: false),
                        ModAmount3 = c.Int(nullable: false),
                        Size = c.Int(nullable: false),
                        Feautre1 = c.String(),
                        Feautre2 = c.String(),
                        Feautre3 = c.String(),
                        Feautre4 = c.String(),
                    })
                .PrimaryKey(t => t.RaceID);
            
            CreateTable(
                "dbo.Themes",
                c => new
                    {
                        ThemeID = c.Int(nullable: false, identity: true),
                        Name = c.String(),
                        Ability = c.String(),
                        Skills = c.String(),
                    })
                .PrimaryKey(t => t.ThemeID);
            
        }
        
        public override void Down()
        {
            DropTable("dbo.Themes");
            DropTable("dbo.Races");
            DropTable("dbo.Classes");
            DropTable("dbo.Characters");
        }
    }
}
