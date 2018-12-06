#!/usr/bin/python
# -*- coding: utf-8 -*-

# gotoclass.py

import wx
import os
import csv

class FileConversion(wx.Frame):
  
    def __init__(self, parent, title):
        super(FileConversion, self).__init__(parent, title=title, 
            size=(390, 400))
        self.dirname=''
                
        self.InitUI()
        self.Centre()
        self.Show()     
        


    def InitUI(self):
        
        wx.Frame(self)
        self.statusbar = self.CreateStatusBar()
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        vcfheader_panel = wx.Panel(self, -1, style=wx.NO_BORDER)
        panel = wx.Panel(self, -1, style=wx.NO_BORDER)
        #pnl3 = wx.Panel(self, -1, style=wx.SUNKEN_BORDER)
        #pnl4 = wx.Panel(self, -1, style=wx.NO_BORDER)

        hbox.Add(vcfheader_panel, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 3)
        hbox.Add(panel, 1, wx.EXPAND | wx.ALL, 3)
        
        #box = wx.BoxSizer(wx.HORIZONTAL)
        
        self.list_box = wx.ListBox(vcfheader_panel, -1, choices=[])
        self.list_box.SetMinSize((150, 363))
        self.button_up = wx.Button(vcfheader_panel, -1, "Up")
        self.button_up.SetMinSize((85, 29))
        self.button_down = wx.Button(vcfheader_panel, -1, "Down")
        self.button_down.SetMinSize((85, 29))
        
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3 = wx.BoxSizer(wx.VERTICAL)
        sizer_2.Add(self.list_box, 0, 0, 0)
        sizer_3.Add(self.button_up, 0, 0, 0)
        sizer_3.Add(self.button_down, 0, 0, 0)
        sizer_2.Add(sizer_3, 1, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_1.Add(sizer_2, 1, wx.ALIGN_CENTER_HORIZONTAL, 0)
        
        ##sizer_14.Add(sizer_15, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        ####widgets
        
        
        #box.Add(self.list_box, 1 )
        #box.Add(self.button_up, 1 )
        #box.Add(self.button_down, 1 )

        
        vcfheader_panel.SetSizer(sizer_1)
        #self.SetSizer(vbox_header)
        #vcfheader_panel.Layout()
        
        
        #######################vcf Panel
        

        font = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
        font.SetPointSize(9)

        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add((-1, 40))
        
        label_csv2vcf = wx.StaticText(panel, label='Convert from VCF to CSV')
        vbox.Add(label_csv2vcf, border=2)
        
        #First Line
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        #Add label
        st1 = wx.StaticText(panel, label='Select your VCF File:')
        st1.SetFont(font)
        hbox1.Add(st1, flag=wx.RIGHT, border=2)
        #Add Field
        self.tc = wx.TextCtrl(panel)
        hbox1.Add(self.tc, proportion=1)
        vbox.Add(hbox1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
        #Add Button
        btn1 = wx.Button(panel, label='Select File', size=(100, -1))
        hbox1.Add(btn1)
        #add vertical space in the bottom
        vbox.Add((-1, 20))

        hbox5 = wx.BoxSizer(wx.HORIZONTAL)
        
        self.btn3 = wx.Button(panel, label='Convert', size=(70, 30))
        hbox5.Add(self.btn3)
        btn4 = wx.Button(panel, label='Close', size=(70, 30))
        hbox5.Add(btn4, flag=wx.LEFT|wx.BOTTOM, border=5)
        vbox.Add(hbox5, flag=wx.ALIGN_RIGHT|wx.RIGHT, border=10)
        
        vbox.Add((-1, 40))
        
        #Second part of the script csv2vcf        
        label_csv2vcf = wx.StaticText(panel, label='Convert from CSV to VCF')
        vbox.Add(label_csv2vcf, border=2)
        
        
        
        linha_box_vcf = wx.BoxSizer(wx.HORIZONTAL)
        #Add label
        label_vcf = wx.StaticText(panel, label='Select your VCF File:')
        label_vcf.SetFont(font)
        linha_box_vcf.Add(label_vcf, flag=wx.RIGHT, border=2)
        #Add Field
        self.field_vcf = wx.TextCtrl(panel)
        linha_box_vcf.Add(self.field_vcf, proportion=1)
        vbox.Add(linha_box_vcf, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
        #Add Button
        button_vcf = wx.Button(panel, label='Select File', size=(100, -1))
        linha_box_vcf.Add(button_vcf)
        
        
        
        linha_box_csv = wx.BoxSizer(wx.HORIZONTAL)
        #Add label
        label_csv = wx.StaticText(panel, label='Select your CSV File:')
        label_csv.SetFont(font)
        linha_box_csv.Add(label_csv, flag=wx.RIGHT, border=2)
        #Add Field
        self.field_csv = wx.TextCtrl(panel)
        linha_box_csv.Add(self.field_csv, proportion=1)
        vbox.Add(linha_box_csv, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
        #Add Button
        button_csv = wx.Button(panel, label='Select File', size=(100, -1))
        linha_box_csv.Add(button_csv)
        
        
        #add vertical space in the bottom
        vbox.Add((-1, 20))
        
        
        
        
        hbox11 = wx.BoxSizer(wx.HORIZONTAL)
        button_csv2vcf_convert = wx.Button(panel, label='Convert', size=(70, 30))
        hbox11.Add(button_csv2vcf_convert)
        button_csv2vcf_close = wx.Button(panel, label='Close', size=(70, 30))
        hbox11.Add(button_csv2vcf_close, flag=wx.LEFT|wx.BOTTOM, border=5)
        vbox.Add(hbox11, flag=wx.ALIGN_RIGHT|wx.RIGHT, border=10)
        
        #add exit event to button
        self.Bind(wx.EVT_BUTTON, self.OnOpen, btn1)
        self.Bind(wx.EVT_BUTTON, self.OnOpen_vcf, button_vcf)
        self.Bind(wx.EVT_BUTTON, self.OnOpen_csv, button_csv)
        
        self.Bind(wx.EVT_BUTTON, self.Vcf2Csv, self.btn3)
        
        self.Bind(wx.EVT_BUTTON, self.Csv2Vcf, button_csv2vcf_convert)
        
        
        self.Bind(wx.EVT_BUTTON, self.OnExit, btn4)
        self.Bind(wx.EVT_BUTTON, self.OnExit, button_csv2vcf_close)
        self.Bind(wx.EVT_BUTTON, self.ButtonUp, self.button_up)
        self.Bind(wx.EVT_BUTTON, self.ButtonDown, self.button_down)
        

        panel.SetSizer(vbox)
        panel.Layout()
        
        self.SetSize((800, 420))
        self.SetSizer(hbox)
        self.Centre()
        
    def OnExit(self,e):
        self.Close(True)  # Close the frame.
    def OnOpen(self,e):
        """ Open a file"""
        dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.vcf", wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            self.tc.SetValue(os.path.join(self.dirname, self.filename))
            #set header values in list
            vcffile = os.path.join(self.dirname, self.filename)
            self.statusbar.SetStatusText('Reading VCF Header...')
            self.btn3.Hide()

            vcf_header_tags = self.Get_vcfheader(vcffile)
            annotation_tags = self.get_all_info_tags(vcffile)
            self.vcf_tag_genotypes = vcf_header_tags[8:]
            vcf_header_tags = vcf_header_tags[:7] + list(annotation_tags)
            
            
            self.list_box.Set(vcf_header_tags)
            
            self.statusbar.SetStatusText('Done...')
            self.btn3.Show()
            
        dlg.Destroy()
    def ButtonUp(self, e):
        
        txt = self.list_box.GetStringSelection()
        pos = self.list_box.GetSelection()
        self.list_box.Delete(pos)
        if pos == 0:
            self.list_box.Insert(txt, self.list_box.GetCount())
            self.list_box.SetSelection(self.list_box.GetCount()-1)
        else:
            self.list_box.Insert(txt, pos-1)
            self.list_box.SetSelection(pos-1)
    def ButtonDown(self, e):
        
        txt = self.list_box.GetStringSelection()
        pos = self.list_box.GetSelection()
        self.list_box.Delete(pos)
        if pos == self.list_box.GetCount():
            self.list_box.Insert(txt, 0)
            self.list_box.SetSelection(0)
        else:
            self.list_box.Insert(txt, pos+1)
            self.list_box.SetSelection(pos+1)
    
        
    def Get_vcfheader(self, filepath):
        vcffile = open(filepath, 'r')
        for line in vcffile:
            if line.startswith("#CHROM"):
                header_tags = line.strip().split('\t')
            if not line.startswith("#"):
                break
        vcffile.close()
        return header_tags
        
    def OnOpen_vcf(self,e):
        """ Open a file"""
        dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.vcf", wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            self.field_vcf.SetValue(os.path.join(self.dirname, self.filename))
            
        dlg.Destroy()
    def OnOpen_csv(self,e):
        """ Open a file"""
        dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.csv", wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            self.field_csv.SetValue(os.path.join(self.dirname, self.filename))
        dlg.Destroy()
        
    #Get all annotation tags from a VCF File reading all file (lazy mode!)
    def get_all_info_tags(self, vcffile):
      tempfile = open(vcffile, 'r')
      annotation_tags = set()
      for line in tempfile:
          if not line.startswith('#'):
              variant = line.split('\t')
              string = variant[7].split(';')
              for element in string:
                  element =  element.split('=')
                  tag = element[0]        
                  if tag not in annotation_tags:
                      annotation_tags.add(tag)
                      
      tempfile.close()
      annotation_tags = sorted(annotation_tags)
      
      return annotation_tags
      
      
    def parse_info_tag(self, string, annotation_tags):
      string = string.split(';')
      information = {}
      for element in string:
          element =  element.split('=')
          tag = element[0]
          if len(element) > 1:
              information[tag] = element[1]
          else:
              information[tag] = 'Yes'
      information_list = []
      for tag in annotation_tags:
          if tag in information:
              information_list.append(str(information[tag]))
          else:
              information_list.append('')
      return information_list
      
    
    def Csv2Vcf(self, e):
      
        
        csvfile = self.field_csv.GetValue()
        vcffile = self.field_vcf.GetValue()
        
        
          
        
        if (vcffile != '') and (csvfile != ''):
            vcffile = open(vcffile, 'r')
            ifile  = open(csvfile, "rb")
            reader = csv.reader(ifile)
            newvcf = open(csvfile+'.new.vcf', 'wb')
            
            self.statusbar.SetStatusText('Converting from CSV to VCF ...')
            #First get header fom VCF
            for line in vcffile:
                if line.startswith('#CHROM'):
                    newvcf.writelines(line.strip())
                elif line.startswith('#'):
                    newvcf.writelines(line)
            vcffile.close()
            #read csv file
            headerline = reader.next()
            
            #print headerline
            
            vcf_header_order = ['#CHROM', 'POS', 'ID', 'REF', 'ALT', 'QUAL', 'FILTER']
            
            format_tag = headerline.index('FORMAT')
            
            
            for row in reader:
                #print row
                tag_list = row[:format_tag]
                #print tag_list
                
                vcfline = []
                for tag in vcf_header_order:
                    index = headerline.index(tag)
                    vcfline.append(tag_list[index])
                variant_annotation = []
                for tag in headerline[:format_tag]:
                    if tag not in vcf_header_order:
                        
                        index = headerline.index(tag)
                        #variant_annotation.append(tag_list[index])
                        if tag_list[index] == 'Yes':
                            variant_annotation.append(tag)
                        elif tag_list[index] != '':
                            variant_annotation.append('%s=%s' % (tag, tag_list[index]))
                
                vcfline.append(";".join(variant_annotation))
                vcfline = vcfline + row[format_tag:]
                #print vcfline, variant_annotation
                #die()
                #print row
                #print tag_string
                
                
                
                
                
                #tag_string = []
                #for tag in infotags:
                    #tag_index = infotags.index(tag)
                    #tag_value = tag_list[tag_index]
                    #if tag_list[tag_index] == 'Yes':
                        #tag_string.append(tag)
                    #elif tag_value != '':
                        #tag_string.append('%s=%s' % (tag, tag_value))
                ##print ";".join(tag_string)
                #vcf_line = "\t".join(row[:7]) + ";".join(tag_string) + "\t".join(row[-stop_tag])
                ##vcf_line = row[:7]
                #vcf_line.append(";".join(tag_string))
                ##print stop_tag
                #vcf_line = vcf_line + row[stop_tag:]
                
                #write line to VCF
                vcf_line_string = "\t".join(vcfline)
                newvcf.writelines('\n'+vcf_line_string)
                
            newvcf.close()
            self.statusbar.SetStatusText('Done, New VCF File Created!')
            wx.MessageBox('File %s.new.vcf was created!' % (csvfile), 'Done', wx.OK | wx.ICON_INFORMATION)
        else:
          wx.MessageBox('You need to select a VCF and CSV File', 'Done', wx.OK | wx.ICON_INFORMATION)
                
                
            
    
    def Vcf2Csv(self, e):
      
      #get full path of file to convert
      vcffile = self.tc.GetValue()
      
      
      if vcffile != '':
        vcf_header = self.list_box.GetStrings() + self.vcf_tag_genotypes
        
        self.statusbar.SetStatusText('Converting...')
        annotation_tags = self.get_all_info_tags(vcffile)
        
        csvfilename = ".".join(os.path.basename(vcffile).split('.')[:-1])+'.csv'
        csvfilepath = os.path.join(os.path.dirname(vcffile), csvfilename)
        
        readfile = open(vcffile, 'r')
        f = open(csvfilepath, "w")
        csvfile = csv.writer(f, quoting=csv.QUOTE_ALL)
        csvfile.writerow(vcf_header)
        for line in readfile:
          if line.startswith('#CHROM'):
            vcf_header_original = line.strip().split('\t')
            vcf_header_original = vcf_header_original[:7] + list(annotation_tags) + vcf_header_original[8:]
          if not line.startswith('#'):
            variant = line.strip().split('\t')
            information = self.parse_info_tag(variant[7], annotation_tags)
            variant = variant[:7] + information + variant[8:]
            new_variant = []
            for tag in vcf_header:
                tag_index = vcf_header_original.index(tag)
                new_variant.append(variant[tag_index])
            csvfile.writerow(new_variant)
        f.close()
        self.statusbar.SetStatusText('Done, CSV File Created! %s' % (csvfilename))
        wx.MessageBox('File %s was created!' % (csvfilename), 'Done', wx.OK | wx.ICON_INFORMATION)
      else:
        wx.MessageBox('You need to select a VCF File first', 'Done', wx.OK | wx.ICON_INFORMATION)
        
if __name__ == '__main__':
    app = wx.App()
    FileConversion(None, title='VCF to CSV File Conversion')
    app.MainLoop()
