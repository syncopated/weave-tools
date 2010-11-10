# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding field 'KeyUnitType.probing_indicator'
        db.add_column('weave_keyunittype', 'probing_indicator', self.gf('django.db.models.fields.related.ForeignKey')(related_name='key_unit_types_as_probe', null=True, to=orm['weave.Indicator']), keep_default=False)
    
    
    def backwards(self, orm):
        
        # Deleting field 'KeyUnitType.probing_indicator'
        db.delete_column('weave_keyunittype', 'probing_indicator_id')
    
    
    models = {
        'weave.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['weave.Category']"})
        },
        'weave.clientconfiguration': {
            'Meta': {'object_name': 'ClientConfiguration'},
            'data_filter': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['weave.DataFilter']"}),
            'default_coloring': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'configs_as_color'", 'null': 'True', 'to': "orm['weave.Indicator']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'years': ('django.db.models.fields.CommaSeparatedIntegerField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'weave.datafilter': {
            'Meta': {'object_name': 'DataFilter'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key_unit_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['weave.KeyUnitType']", 'null': 'True'}),
            'keys_query': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        'weave.indicator': {
            'Meta': {'object_name': 'Indicator'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'indicators'", 'null': 'True', 'to': "orm['weave.Category']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key_field_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'key_unit_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['weave.KeyUnitType']", 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'table_name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'weave.keyunittype': {
            'Meta': {'object_name': 'KeyUnitType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'probing_indicator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'key_unit_types_as_probe'", 'null': 'True', 'to': "orm['weave.Indicator']"})
        },
        'weave.layout': {
            'Meta': {'object_name': 'Layout'},
            'config_template': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        'weave.row': {
            'Meta': {'object_name': 'Row'},
            'config': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'rows'", 'to': "orm['weave.ClientConfiguration']"}),
            'height': ('weave.fields.PercentField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'width': ('weave.fields.PercentField', [], {})
        },
        'weave.tool': {
            'Meta': {'object_name': 'Tool'},
            'barChartTitle': ('django.db.models.fields.CharField', [], {'default': "'Bar Chart'", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'binAttribute': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'tools_as_bin'", 'null': 'True', 'to': "orm['weave.Indicator']"}),
            'colorAttribute': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'tools_as_color'", 'null': 'True', 'to': "orm['weave.Indicator']"}),
            'data_filter': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['weave.DataFilter']", 'null': 'True', 'blank': 'True'}),
            'height': ('weave.fields.PercentField', [], {}),
            'heightAttribute': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'tools_as_height'", 'null': 'True', 'to': "orm['weave.Indicator']"}),
            'histogramTitle': ('django.db.models.fields.CharField', [], {'default': "'Histogram'", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mapTitle': ('django.db.models.fields.CharField', [], {'default': "'Rhode Island'", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'row': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tools'", 'to': "orm['weave.Row']"}),
            'sortingAttribute': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'tools_as_sorting'", 'null': 'True', 'to': "orm['weave.Indicator']"}),
            'table_columns': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'tools_as_table_column'", 'blank': 'True', 'to': "orm['weave.Indicator']"}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'width': ('weave.fields.PercentField', [], {}),
            'xAttribute': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'tools_as_x'", 'null': 'True', 'to': "orm['weave.Indicator']"}),
            'yAttribute': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'tools_as_y'", 'null': 'True', 'to': "orm['weave.Indicator']"})
        }
    }
    
    complete_apps = ['weave']