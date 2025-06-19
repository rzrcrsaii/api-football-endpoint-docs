#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
API Football Endpoint Dokümantasyon Birleştirici
Bu script, mevcut dizindeki tüm dosyaları tarayarak tek bir Markdown dosyasında birleştirir.
"""

import os
import sys
from pathlib import Path
import mimetypes
from datetime import datetime

class DocumentationMerger:
    def __init__(self, output_file="all-in-one.md"):
        self.output_file = output_file
        self.script_file = Path(__file__).name  # Script dosyasının adını al
        self.processed_files = 0
        self.skipped_files = 0
        self.error_files = 0
        self.binary_extensions = {
            '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.ico', '.svg',
            '.mp4', '.avi', '.mov', '.wmv', '.flv', '.webm',
            '.mp3', '.wav', '.flac', '.aac', '.ogg',
            '.zip', '.rar', '.7z', '.tar', '.gz',
            '.exe', '.dll', '.so', '.dylib',
            '.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx'
        }
        self.skip_patterns = {
            '.git', '.vscode', '.idea', '__pycache__', 'node_modules',
            '.tmp', '.temp', '.log', '.cache', '.DS_Store', 'Thumbs.db'
        }
        
    def should_skip_file(self, file_path):
        """Dosyanın atlanıp atlanmayacağını kontrol eder"""
        file_name = file_path.name

        # Script dosyasının kendisini atla
        if file_name == self.script_file:
            return True

        # Çıktı dosyasını atla (eğer zaten varsa)
        if file_name == self.output_file:
            return True

        # Gizli dosyalar ve klasörler
        if file_name.startswith('.'):
            return True

        # Skip patterns kontrolü
        for pattern in self.skip_patterns:
            if pattern in str(file_path):
                return True

        # Binary dosya kontrolü
        file_extension = file_path.suffix.lower()
        if file_extension in self.binary_extensions:
            return True

        # MIME type kontrolü
        mime_type, _ = mimetypes.guess_type(str(file_path))
        if mime_type and not mime_type.startswith('text/'):
            return True

        return False
    
    def get_file_language(self, file_path):
        """Dosya uzantısına göre syntax highlighting dili belirler"""
        extension = file_path.suffix.lower()
        language_map = {
            '.py': 'python',
            '.js': 'javascript',
            '.ts': 'typescript',
            '.html': 'html',
            '.css': 'css',
            '.json': 'json',
            '.xml': 'xml',
            '.yaml': 'yaml',
            '.yml': 'yaml',
            '.md': 'markdown',
            '.sh': 'bash',
            '.bat': 'batch',
            '.sql': 'sql',
            '.php': 'php',
            '.java': 'java',
            '.cpp': 'cpp',
            '.c': 'c',
            '.cs': 'csharp',
            '.go': 'go',
            '.rs': 'rust',
            '.rb': 'ruby',
            '.txt': 'text'
        }
        return language_map.get(extension, 'text')
    
    def read_file_content(self, file_path):
        """Dosya içeriğini güvenli şekilde okur"""
        encodings = ['utf-8', 'utf-8-sig', 'latin-1', 'cp1252']
        
        for encoding in encodings:
            try:
                with open(file_path, 'r', encoding=encoding) as f:
                    return f.read()
            except UnicodeDecodeError:
                continue
            except Exception as e:
                print(f"❌ Hata: {file_path} dosyası okunamadı - {str(e)}")
                return None
        
        print(f"❌ Hata: {file_path} dosyası hiçbir encoding ile okunamadı")
        return None
    
    def process_file(self, file_path, output_file):
        """Tek bir dosyayı işler ve output dosyasına yazar"""
        print(f"📄 İşleniyor: {file_path}")
        
        # Dosya içeriğini oku
        content = self.read_file_content(file_path)
        if content is None:
            self.error_files += 1
            return
        
        # Relative path hesapla
        try:
            relative_path = file_path.relative_to(Path.cwd())
        except ValueError:
            relative_path = file_path
        
        # Dosya başlığı
        output_file.write(f"\n## {relative_path}\n\n")
        
        # Dosya bilgileri
        file_size = file_path.stat().st_size
        modified_time = datetime.fromtimestamp(file_path.stat().st_mtime)
        output_file.write(f"**Dosya Boyutu:** {file_size} bytes  \n")
        output_file.write(f"**Son Değişiklik:** {modified_time.strftime('%Y-%m-%d %H:%M:%S')}  \n\n")
        
        # İçerik
        language = self.get_file_language(file_path)
        output_file.write(f"```{language}\n")
        output_file.write(content)
        if not content.endswith('\n'):
            output_file.write('\n')
        output_file.write("```\n\n")
        
        # Ayırıcı
        output_file.write("---\n\n")
        
        self.processed_files += 1
    
    def scan_directory(self, directory_path):
        """Dizini tarar ve tüm dosyaları listeler"""
        all_files = []
        
        for root, dirs, files in os.walk(directory_path):
            # Gizli klasörleri atla
            dirs[:] = [d for d in dirs if not d.startswith('.') and d not in self.skip_patterns]
            
            root_path = Path(root)
            
            for file_name in files:
                file_path = root_path / file_name
                
                if not self.should_skip_file(file_path):
                    all_files.append(file_path)
                else:
                    # Atlanan dosya türüne göre farklı mesajlar
                    if file_path.name == self.script_file:
                        print(f"⏭️  Script dosyası atlandı: {file_path}")
                    elif file_path.name == self.output_file:
                        print(f"⏭️  Çıktı dosyası atlandı: {file_path}")
                    elif file_path.suffix.lower() in self.binary_extensions:
                        print(f"⏭️  Binary dosya atlandı: {file_path}")
                    else:
                        print(f"⏭️  Gizli/geçici dosya atlandı: {file_path}")
                    self.skipped_files += 1
        
        return sorted(all_files)
    
    def create_documentation(self, source_directory="."):
        """Ana dokümantasyon oluşturma fonksiyonu"""
        print("🚀 API Football Endpoint Dokümantasyon Birleştirici Başlatılıyor...")
        print(f"📁 Kaynak Dizin: {os.path.abspath(source_directory)}")
        print(f"📝 Çıktı Dosyası: {self.output_file}")
        print("=" * 60)
        
        # Dosyaları tara
        print("🔍 Dosyalar taranıyor...")
        all_files = self.scan_directory(source_directory)
        
        if not all_files:
            print("❌ İşlenecek dosya bulunamadı!")
            return
        
        print(f"✅ {len(all_files)} dosya işlenmeye hazır")
        print("=" * 60)
        
        # Output dosyasını oluştur
        try:
            with open(self.output_file, 'w', encoding='utf-8') as output_file:
                # Başlık ve metadata
                output_file.write("# API Football Endpoint Dokümantasyonu\n\n")
                output_file.write(f"**Oluşturulma Tarihi:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  \n")
                output_file.write(f"**Toplam Dosya Sayısı:** {len(all_files)}  \n")
                output_file.write(f"**Kaynak Dizin:** {os.path.abspath(source_directory)}  \n\n")
                
                # İçindekiler
                output_file.write("## İçindekiler\n\n")
                for file_path in all_files:
                    try:
                        relative_path = file_path.relative_to(Path.cwd())
                    except ValueError:
                        relative_path = file_path
                    output_file.write(f"- [{relative_path}](#{str(relative_path).replace('/', '').replace('\\', '').replace('.', '').replace(' ', '-').lower()})\n")
                output_file.write("\n---\n\n")
                
                # Dosyaları işle
                for file_path in all_files:
                    try:
                        self.process_file(file_path, output_file)
                    except Exception as e:
                        print(f"❌ Hata: {file_path} işlenirken hata oluştu - {str(e)}")
                        self.error_files += 1
                        continue
                
                # Footer
                output_file.write(f"\n---\n\n")
                output_file.write(f"**Dokümantasyon Özeti:**  \n")
                output_file.write(f"- İşlenen Dosyalar: {self.processed_files}  \n")
                output_file.write(f"- Atlanan Dosyalar: {self.skipped_files}  \n")
                output_file.write(f"- Hatalı Dosyalar: {self.error_files}  \n")
                output_file.write(f"- Oluşturulma Tarihi: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  \n")
        
        except Exception as e:
            print(f"❌ Kritik Hata: Output dosyası oluşturulamadı - {str(e)}")
            return
        
        # Sonuç raporu
        print("=" * 60)
        print("✅ Dokümantasyon başarıyla oluşturuldu!")
        print(f"📊 İşlem Raporu:")
        print(f"   • İşlenen dosyalar: {self.processed_files}")
        print(f"   • Atlanan dosyalar: {self.skipped_files}")
        print(f"   • Hatalı dosyalar: {self.error_files}")
        print(f"📁 Çıktı dosyası: {os.path.abspath(self.output_file)}")
        print(f"📏 Dosya boyutu: {os.path.getsize(self.output_file)} bytes")

def main():
    """Ana fonksiyon"""
    merger = DocumentationMerger()
    merger.create_documentation()

if __name__ == "__main__":
    main()
