namespace StarfinderSRD.Migrations
{
    using StarfinderSRDModelBinding.Models;
    using System;
    using System.Data.Entity;
    using System.Data.Entity.Migrations;
    using System.Linq;

    internal sealed class Configuration : DbMigrationsConfiguration<StarfinderSRDModelBinding.Models.CharacterContext>
    {
        public Configuration()
        {
            AutomaticMigrationsEnabled = false;
        }

        protected override void Seed(StarfinderSRDModelBinding.Models.CharacterContext context)
        {
            context.Characters.AddOrUpdate(
                 new Character
                 {
                     Name = "kAPP",
                     Race = "Android",
                     Class = "Mechanic",
                     Theme = "Tinkerer"
                 },
                 new Character
                 {
                     Name = "Dennea Fon",
                     Race = "Lashunta",
                     Class = "Solarian",
                     Theme = "Ace Pilot"
                 },
                 new Character
                 {
                     Name = "Reticent Stroidjumper",
                     Race = "Halfling",
                     Class = "Operative",
                     Theme = "Grifter"
                 },
                 new Character
                 {
                     Name = "Rurick Brom",
                     Race = "Dwarf",
                     Class = "Soldier",
                     Theme = "Guard"
                 },
                 new Character
                 {
                     Name = "Rayraj Vymm",
                     Race = "Tiefling",
                     Class = "Envoy",
                     Theme = "Icon"
                 },
                 new Character
                 {
                     Name = "Wix Nagla",
                     Race = "Stellafera",
                     Class = "Mystic",
                     Theme = "Cultist"
                 },
                 new Character
                 {
                     Name = "Dr. Xiago",
                     Race = "Skittermander",
                     Class = "Biohacker",
                     Theme = "Battle Medic"
                 }
                 );

            context.SaveChanges();

            context.Races.AddOrUpdate(
                new Race { Name = "Android", HP = 4 },
                new Race { Name = "Lashunta", HP = 4 },
                new Race { Name = "Halfling", HP = 2 },
                new Race { Name = "Dwarf", HP = 6 },
                new Race { Name = "Tiefling", HP = 4 },
                new Race { Name = "Stellafera", HP = 2 },
                new Race { Name = "Skittermander", HP = 2 }
                );

            context.SaveChanges();

            context.Classes.AddOrUpdate(
                new Class { Name = "Mechanic", HPSP = 6, SkillPoints = 4 },
                new Class { Name = "Solarian", HPSP = 7, SkillPoints = 4 },
                new Class { Name = "Operative", HPSP = 6, SkillPoints = 8 },
                new Class { Name = "Soldier", HPSP = 7, SkillPoints = 4 },
                new Class { Name = "Envoy", HPSP = 6, SkillPoints = 8 },
                new Class { Name = "Mystic", HPSP = 6, SkillPoints = 8 },
                new Class { Name = "Biohacker", HPSP = 6, SkillPoints = 4 }
                );

            context.SaveChanges();

            context.Themes.AddOrUpdate(
                new Theme { Name = "Tinkerer" },
                new Theme { Name = "Ace Pilot" },
                new Theme { Name = "Grifter" },
                new Theme { Name = "Guard" },
                new Theme { Name = "Icon" },
                new Theme { Name = "Cultist" },
                new Theme { Name = "Battle Medic" }
                );

            context.SaveChanges();
        }
    }
}
