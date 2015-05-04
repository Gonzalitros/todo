class CreateRaces < ActiveRecord::Migration
  def change
    create_table :races do |t|
      t.string :title
      t.string :country

      t.timestamps
    end
  end
end
